import numpy as np
import time
import cv2
import tensorflow as tf

def loss(self, net_out):
	m = self.meta
	loss_type = self.meta['type']
	assert loss_type in _LOSS_TYPE, \
	'Loss type {} not implemented'.format(loss_type)

	out = net_out
	out_shape = out.get_shape()
	out_dtype = out.dtype.base_dtype
	_truth = tf.placeholders(out_dtype, out_shape)

	self.placeholders = dict({
			'truth': _truth
		})

	diff = _truth - out
	if loss_type in ['sse','12']:
		loss = tf.nn.l2_loss(diff)

	elif loss_type == ['smooth']:
		small = tf.cast(diff < 1, tf.float32)
		large = 1. - small
		l1_loss = tf.nn.l1_loss(tf.multiply(diff, large))
		l2_loss = tf.nn.l2_loss(tf.multiply(diff, small))
		loss = l1_loss + l2_loss

	elif loss_type in ['sparse', 'l1']:
		loss = l1_loss(diff)

	elif loss_type == 'softmax':
		loss = tf.nn.softmax_cross_entropy_with_logits(logits, y)
		loss = tf.reduce_mean(loss)

	elif loss_type == 'svm':
		assert 'train_size' in m, \
		'Must specify'
		size = m['train_size']
		self.nu = tf.Variable(tf.ones([train_size, num_classes]))

def make_img(colors,results,depth_colormap):
    for color,result in zip(colors,results):
        if result['label']=="person":
            tl = (result['topleft']['x'],result['topleft']['y'])
            br = (result['bottomright']['x'],result['bottomright']['y'])
            label = result['label']
            depth_colormap = cv2.rectangle(depth_colormap,tl,br,color,7)
            depth_colormap = cv2.putText(depth_colormap,label,tl,cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,0),2)   
    return depth_colormap
