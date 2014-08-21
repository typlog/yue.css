build:
	@myth < index.css > yue.css
	@# ensure it has a new line at end of file
	@echo '' >> yue.css

watch:
	@rewatch index.css -c "make build"

.PHONY: watch build
