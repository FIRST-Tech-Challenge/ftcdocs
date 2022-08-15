Machine Learning In a Nutshell 
==============================

What is Machine Learning? Machine learning is a branch of Artificial
Intelligence (AI) and computer science which focuses on the use of data
and algorithms to imitate the way humans learn, gradually improving its
accuracy. To borrow a description from TensorFlow’s “\ `Intro to Machine
Learning <https://www.youtube.com/watch?v=KNAWp2S3w94>`__\ ” video
series, traditional programming involves programming complex rules into
a computer program that are used to analyze input data and output an
answer. If the input data is an image of a flower, and if the
programming/rules can recognize the flower, then it outputs the answer
“flower.” Having a traditional program recognize the differences between
multiple different kinds of flowers would require significantly more
complex programming, especially if the images are allowed to be at
various angles and orientations, and not directly centered in the image.
Instead, machine learning focuses on providing examples to a machine
learning algorithm or “model” – providing data **and** answers – and
allowing the model to build its own rules to determine the relationships
between the examples provided to it. Just like a human, during each
“step” of the training process the model makes a refined guess about the
relationships between the known examples and then tests those guesses
against examples not yet seen. By training a model over successive
steps, the model attempts to improve its accuracy in correctly
identifying previously unseen variations of the data. In this way,
training a model to correctly recognize multiple types of data requires
no more source code than recognizing a single type, it only requires
creating more examples for the model to learn.

In *FIRST* Tech Challenge, the machine learning platform used is
`TensorFlow <https://www.tensorflow.org/>`__. TensorFlow is an open
source platform for machine learning with a comprehensive, flexible
ecosystem of tools, libraries, and community resources to enable
developers to create tools such as the *FIRST* Tech Challenge Machine
Learning tool. TensorFlow has been utilized in *FIRST* Tech Challenge
for a number of years, allowing teams to recognize individual game
pieces and clusters of game pieces via pre-built models developed by
*FIRST* Tech Challenge engineers. Now *FIRST* Tech Challenge is
empowering teams to build their own custom models!