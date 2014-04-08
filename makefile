commit:
	git add -A -v
	git commit -m "$M"

push:
	git push -u origin master

commit-and-push:
	make M="$M" commit
	make push

