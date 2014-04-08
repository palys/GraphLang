commit:
	git add -A -v
	git commit -m "$M"

push:
	git push -u origin master

push-and-commit:
	make M=$M commit
	make push

