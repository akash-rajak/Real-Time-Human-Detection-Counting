
# from random import randint
# from collections import OrderedDict
# from scipy.spatial import distance as dist
# import cv2 as cv
import numpy as np
import tensorflow as tf
# import cv2
import time
import os
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# class TrackableObject:
#     def __init__(self, objectID, centroid):
#         self.objectID = objectID
#         self.centroids = [centroid]
#         self.counted = False
#
# class CentroidTracker:
#     def __init__(self, maxDisappeared=50, maxDistance=50):
#         self.nextObjectID = 0
#         self.objects = OrderedDict()
#         self.disappeared = OrderedDict()
#         self.maxDisappeared = maxDisappeared
#         self.maxDistance = maxDistance
#
#     def register(self, centroid):
#         self.objects[self.nextObjectID] = centroid
#         self.disappeared[self.nextObjectID] = 0
#         self.nextObjectID += 1
#
#     def deregister(self, objectID):
#         del self.objects[objectID]
#         del self.disappeared[objectID]
#
#     def update(self, rects):
#         if len(rects) == 0:
#             for objectID in list(self.disappeared.keys()):
#                 self.disappeared[objectID] += 1
#                 if self.disappeared[objectID] > self.maxDisappeared:
#                     self.deregister(objectID)
#             return self.objects
#
#         inputCentroids = np.zeros((len(rects), 2), dtype="int")
#
#         for (i, (startX, startY, endX, endY)) in enumerate(rects):
#             cX = int((startX + endX) / 2.0)
#             cY = int((startY + endY) / 2.0)
#             inputCentroids[i] = (cX, cY)
#         if len(self.objects) == 0:
#             for i in range(0, len(inputCentroids)):
#                 self.register(inputCentroids[i])
#         else:
#             objectIDs = list(self.objects.keys())
#             objectCentroids = list(self.objects.values())
#             D = dist.cdist(np.array(objectCentroids), inputCentroids)
#             rows = D.min(axis=1).argsort()
#             cols = D.argmin(axis=1)[rows]
#             usedRows = set()
#             usedCols = set()
#
#             for (row, col) in zip(rows, cols):
#                 if row in usedRows or col in usedCols:
#                     continue
#                 if D[row, col] > self.maxDistance:
#                     continue
#                 objectID = objectIDs[row]
#                 self.objects[objectID] = inputCentroids[col]
#                 self.disappeared[objectID] = 0
#                 usedRows.add(row)
#                 usedCols.add(col)
#
#             unusedRows = set(range(0, D.shape[0])).difference(usedRows)
#             unusedCols = set(range(0, D.shape[1])).difference(usedCols)
#             if D.shape[0] >= D.shape[1]:
#                 for row in unusedRows:
#                     objectID = objectIDs[row]
#                     self.disappeared[objectID] += 1
#                     if self.disappeared[objectID] > self.maxDisappeared:
#                         self.deregister(objectID)
#             else:
#                 for col in unusedCols:
#                     self.register(inputCentroids[col])
#         return self.objects

class DetectorAPI:
    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__))
        self.path_to_ckpt = f'frozen_inference_graph.pb'
        self.detection_graph = tf.Graph()

        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.path_to_ckpt, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        self.default_graph = self.detection_graph.as_default()
        self.sess = tf.Session(graph=self.detection_graph)

        # Definite input and output Tensors for detection_graph
        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

    def processFrame(self, image):
        # Expand dimensions since the trained_model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image, axis=0)
        # Actual detection.
        start_time = time.time()
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores,
                self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})
        end_time = time.time()

        # print("Elapsed Time:", end_time-start_time)
        # print(self.image_tensor, image_np_expanded)
        im_height, im_width, _ = image.shape
        boxes_list = [None for i in range(boxes.shape[1])]

        for i in range(boxes.shape[1]):
            boxes_list[i] = (int(boxes[0, i, 0] * im_height),int(boxes[0, i, 1]*im_width),int(boxes[0, i, 2] * im_height),int(boxes[0, i, 3]*im_width))

        return boxes_list, scores[0].tolist(), [int(x) for x in classes[0].tolist()], int(num[0])

    def close(self):
        self.sess.close()
        self.default_graph.close()