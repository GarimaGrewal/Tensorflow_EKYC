
# coding: utf-8

# In[ ]:


import tensorflow as tf
import sys
import time
start_time = time.time()

# change this as you see fit
image_path = sys.argv[1]
#image_path = raw_input("Enter the image path:")

# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("/home/garima/Documents/myclassifier/retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("/home/garima/Documents/myclassifier/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
    predictions = sess.run(softmax_tensor,              {'DecodeJpeg/contents:0': image_data})
    
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    firstElt = top_k[0];
        
    str2=" "

    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        if (human_string=="aadhar" and score>.8):
            str2 = str2 + human_string + " ( "+ str(score*100)+"% )" 
            
            print('%s (score = %.5f)' % (human_string, score))
        elif (human_string=="pan card" and score>.7):
            str2 = str2 + human_string + " ( "+ str(score*100)+"% )"
            
            print('%s (score = %.5f)' % (human_string, score))
        elif (human_string=="passport" and score>.7):
            str2 = str2 + human_string + " ( "+ str(score*100)+"% )" 
	   
            print('%s (score = %.5f)' % (human_string, score))
        elif (human_string=="unacceptable id" and score>.6):
            str2 = str2 + human_string + " ( "+ str(score*100)+"% )"
           
            print('%s (score = %.5f)' % (human_string, score))
        #return human_string
        #print (node_id)
        #print('%s (score = %.5f)' % (human_string, score))
    if (str2 ==  " "):
     	print("sorry, cant classify")
        #return render_template('upload_file.html', strng=strng)
       
    #strng= strng +" | "+ human_string +"("+ str(score*100)+"%)"
    #strng = strng + str2 + "| Time = "+ str(time.time() - start_time) + "sec"
    
    print("--- %s seconds ---" % (time.time() - start_time))	

