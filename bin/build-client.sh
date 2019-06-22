#! /usr/bin/env bash

# brew install swagger-codegen

docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -l python \
    -i http://localhost:5000/api/v1/openapi.json \
    -o ./temp-client \
    -c client-config.json

rm -rf pybloods/client
mkdir -p pybloods/client
rsync -a ./temp-client/client/ ./pybloods/client/

(cd ./temp-client && mv README.md docs ../pybloods/client)
# rm -rf ./temp-client
