#! /bin/bash

set -x

cd cem/data/CUB200
wget -q --show-progress -O CUB_200_2011.tar.gz "https://worksheets.codalab.org/rest/bundles/0xd013a7ba2e88481bbc07e787f73109f5/contents/blob/"
mkdir -p CUB_200_2011 && tar -zxf CUB_200_2011.tar.gz -C CUB_200_2011