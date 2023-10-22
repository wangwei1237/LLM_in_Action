#!/bin/bash

set -ex

if [ $# -ne 3 ]
then
    echo "::error the parameters error, please check!!!"
    exit 1
fi

URL_PREFIX="https://api.github.com/repos/wangwei1237/LLM_in_Action/releases"

version=$1
token=$2
notes="$3"

get_release_url="${URL_PREFIX}/tags/${version}"
upload_url=$(curl -H "Accept: application/vnd.github.v3+json" "${get_release_url}" | grep 'upload_url' | cut -d'"' -f4)

create_release_url="${URL_PREFIX}"
if [ "$upload_url" = "" ]
then
    upload_url=$(curl -X POST -H "Accept: application/vnd.github.v3+json" "${create_release_url}" -H "Authorization: token ${token}" -d "{\"tag_name\":\"${version}\", \"name\":\"Build for ${version}\", \"body\":\"${notes}\"}" | grep 'upload_url' | cut -d'"' -f4)
fi

if [ "$upload_url" = "" ]
then
    echo "::error create release error, please check!!!"
    exit 1
fi

echo $upload_url
