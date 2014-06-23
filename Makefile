shorthash=$(shell git rev-parse --short HEAD)

# initial `gh-pages` branch created with:
#
# git checkout --orphan gh-pages
# git rm -rf .
# touch .nojekyll
# git add .
# git commit -m "initial pages commit" --allow-empty

# TODO make sure local gh-pages is up to date with remote. Right now, it fails,
# which is fine.
#
# TODO delete old files
#
# Uses `cp` because `mv` is too brittle
docs:
	cd docs && $(MAKE) html
	git checkout gh-pages
	cp -r docs/_build/html/* .
	git add .
	git reset -- docs/
	git commit -m "build docs based on $(shorthash)"
	git push origin gh-pages
	git checkout -

.PHONY: docs
