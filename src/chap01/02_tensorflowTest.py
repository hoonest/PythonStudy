import tensorflow as tf

print(tf.__version__)

hello = tf.constant('Hello, Tensorflow!!!')

sess = tf.Session()

print(sess.run(hello))