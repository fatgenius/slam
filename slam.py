#!/usr/bin/env python
# -*- coding: utf-8 -*- 

 
import cv2
import pygame
import time
from display import Display
from extractor import Extractor
import numpy as np


W = 1920//2
H = 1080//2

##pygame.init()
##screen = pygame.display.set_mode((W,H))

#surface = pygame.surface(W,H).convert()


#cv2.namedWindow('image',cv2.WINDOW_NORMAL)

 


disp =Display(W,H)
# fe = Extractor()
#orb = cv2.ORB_create()
#print(dir(orb))


class FeatureExtractor(object):
	"""docstring for FeatureExtractor"""
	# put image into small grid

	# GX = 16
	# GY = 16

	def __init__(self):
		self.orb =cv2.ORB_create(100)
	def extract(self, img):
		feats = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3) 
		kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1],_size =20) for f in feats]
		des =self.orb.compute(img,kps)
		"""
		if self.last is not None:
			matches =self.bf.match(des, self.last['kps'])
			print(matches)


		self.last ={'kps':kps,'des':des}
		"""
		return kps, des

		 # run detect in grid
		# sy = img.shape[0]//self.GY
		# sx = img.shape[1]//self.GX
		# for ry in range(0,img.shape[0],sy):
		# 	for rx in range(0,img.shape[1],sx):
		# 		img_chunk =img[ry:ry+sy, rx:rx+sx]
		# 		kp, des = self.orb.detect(img_chunk ,None)
		# 		for p in kp:
		# 			print(p)
		
fe = FeatureExtractor()

def process_frame(img):
	img =cv2.resize(img,(W,H))
	kps, des =fe.extract(img)
	for i in kps:
	  u,v=map(lambda x: int(round(x)),i.pt)
	  cv2.circle(img,(u,v),color=(0,255,0),radius =3)
	disp.paint(img)	
# def process_frame(img):
# 	matches = fe.extract(img)
# 	print("%d matches" % (len(matches)))
# 	for pt1, pt2 in matches:
# 	  	u1,v1 = map(lambda x: int(round(x)),pt1)

# 	  	u2,v2 = map(lambda x: int(round(x)),pt2) 
# 	  	cv2.circle(img, (u1, v1), color=(0,255,0), radius=3)
# 	  	cv2.line(img, (u1, v1), (u2, v2), color=(255,0,0))
	 
# 	disp.paint(img)

##	surf =pygame.surfarray.make_surface(img.swapaxes(0,1)).convert()
##	print(surf)
##	screen.blit(surf,(0,0))
##	pygame.display.update()
##	time.sleep(1)
#	cv2.imshow('image',img) 
#	cv2.waitKey()	
##	print(img.shape)



if __name__=="__main__":
	cap = cv2.VideoCapture("test.mp4")

	while cap.isOpened():
		ret, frame =cap. read()
		if ret == True:
			process_frame(frame)
		else:
			break


