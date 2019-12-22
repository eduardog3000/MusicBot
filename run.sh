git reset --hard origin/master

git stash
git stash drop

git pull

python3 -V > /dev/null 2>&1 || {
	echo >&2 "Python 3 doesn't seem to be installed."
	exit 1; }

python3 -m pip install -U -r requirements.txt

screen -S "WholesomeBot" python3 run.py
		
