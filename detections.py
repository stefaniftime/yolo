for file in glob.glob(path):
    print(file)
    !./darknet detector test data/obj.data cfg/yolov4_custom.cfg /mydrive/ColabNotebooks/yolov4/backup/yolov4_custom_best.weights "$file" -thresh 0.3 -dont_show
    !cp -r 'predictions.jpg' /mydrive/ColabNotebooks/yolov4/detections
    os.rename('/mydrive/ColabNotebooks/yolov4/detections/predictions.jpg','/mydrive/ColabNotebooks/yolov4/detections/' + file[27:-4] + '.jpg')
    imShow('predictions.jpg')
