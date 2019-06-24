clientpy: check-env
	docker run \
	    --rm -v ${PWD}:/local \
	    openapitools/openapi-generator-cli generate \
            -i http://${API_SERVER}/api/v1/openapi.json \
            -g python \
            -o /local/pybloods-client \
            -DpackageName=pybloodsclient && \
    sudo chown -R $(USER) ./pybloods-client && \
    rsync -avz pybloods-client/ ${CLIENT_DIR} && \
    rm -rf pybloods-client/

jsclient: check-env
    docker run \
        --rm -v ${PWD}/pybloods/gui/js:/local \
	    openapitools/openapi-generator-cli generate \
            -i http://${API_SERVER}/api/v1/openapi.json \
            -g javascript \
            -o /local/pybloods-client
check-env:
ifndef API_SERVER
	$(error API_SERVER is undefined)
endif

ifndef CLIENT_DIR
	$(error CLIENT_DIR is undefined)
endif
