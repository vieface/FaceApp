cp -r device_application/__pycache__/* device_application/
cd device_application
rm -f main_frame.py
rm -f sleep_frame.py
rm -f proces_app.py
rm -f schedule_restart.py
mv main_frame.cpython-36.pyc main_frame.pyc
mv sleep_frame.cpython-36.pyc sleep_frame.pyc
mv process_app.cpython-36.pyc process_app.pyc
mv schedule_restart.cpython-36.pyc schedule_restart.pyc
rm -rf __pycache__/

cp -r utils/__pycache__/* utils/
rm -f utils/*.py
rm -rf utils/__pycache__/

cd utils
mv utils.cpython-36.pyc utils.pyc
mv graphic.cpython-36.pyc graphic.pyc
mv mapping.cpython-36.pyc mapping.pyc
mv prs.cpython-36.pyc prs.pyc
mv prs_app.cpython-36.pyc prs_app.pyc
mv reques2api.cpython-36.pyc reques2api.pyc
mv widgets.cpython-36.pyc widgets.pyc
mv objects.cpython-36.pyc objects.pyc

cd ..

cp -r detection/__pycache__/* detection/
cd detection
rm -f *.py
mv ultra_face_opencvdnn_inference.cpython-36.pyc ultra_face_opencvdnn_inference.pyc
rm -rf __pycache__/


