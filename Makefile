client: check-env
	swagger-codegen \
		generate \
		-i http://${API_SERVER}/api/v1/openapi.json \
		-l python \
		-o ${CLIENT_DIR} \
		-DpackageName=pybloodsclient


check-env:
ifndef API_SERVER
	$(error API_SERVER is undefined)
endif

ifndef CLIENT_DIR
	$(error CLIENT_DIR is undefined)
endif
