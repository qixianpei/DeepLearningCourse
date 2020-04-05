import tensorflow as tf
import numpy as np
x=tf.constant(np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]))
y=tf.constant(np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]))
x1=tf.reduce_mean(x)
y1=tf.reduce_mean(y)
x2=x-x1
y2=y-y1
x3=tf.square(x2)
w=(tf.reduce_sum(x2*y2))/(tf.reduce_sum(x3))
b=y1-w*x1
print("w=%f"%w)
print("b=%f"%b)