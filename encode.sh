pip3 install pyarmor
pyarmor obfuscate run.py 

cd utils
pyarmor obfuscate prs.py

mv dist utils 

cd ..

cd detection 
pyarmor obfuscate ultra_face_opencvdnn_inference.py
mv dist detection

cd ..

mkdir dist/utils
mkdir dist/detection
mkdir dist/model 
mkdir dist/dataset

cp -R utils/utils/* dist/utils/
rm -rf utils/utils

cp -R  detection/detection/* dist/detection 
rm -rf detection/detection


cp -R  model/* dist/model
cp -R  dataset/* dist/dataset


cd .. 

mkdir device_application_encode

cp -R device_application/dist/* device_application_encode/

rm -rf device_application

mv device_application_encode device_application

cd device_application

python3 run.py



