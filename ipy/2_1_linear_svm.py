{
 "metadata": {
  "name": "2_supervised_learning"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Supervised Learning: SVM\n",
      "========================\n",
      "\n",
      "\n",
      "Run the following code fragments in order to train an SVM."
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# initialize the workspace by importing several symbols\n",
      "import logging\n",
      "import sys\n",
      "import time\n",
      "\n",
      "import numpy as np\n",
      "from numpy import arange, dot, maximum, ones, tanh, zeros\n",
      "from numpy.random import randn\n",
      "\n",
      "from skdata import mnist\n",
      "import autodiff\n",
      "\n",
      "from util import show_filters\n",
      "#from utils import show_filters"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# -- load and prepare the data set (even download if necessary)\n",
      "dtype = 'float32'\n",
      "n_examples = 10000\n",
      "n_classes = 10\n",
      "img_shape = (28, 28)\n",
      "\n",
      "data_view = mnist.views.OfficialVectorClassification(x_dtype=dtype)\n",
      "x = data_view.train.x[:n_examples]\n",
      "y = data_view.train.y[:n_examples]\n",
      "\n",
      "# -- prepare a \"1-hot\" version of the labels\n",
      "y1 = -1 * ones((len(y), n_classes)).astype(dtype)\n",
      "y1[arange(len(y)), y] = 1"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# -- initialize the SVM model\n",
      "w = zeros((x.shape[1], n_classes), dtype=dtype)\n",
      "b = zeros(n_classes, dtype=dtype)\n",
      "\n",
      "def svm(ww, bb, xx=x, yy=y1):\n",
      "    # -- one vs. all linear SVM loss\n",
      "    margin = yy * (dot(xx, ww) + bb)\n",
      "    hinge = maximum(0, 1 - margin)\n",
      "    cost = hinge.mean(axis=0).sum()\n",
      "    return cost\n",
      "\n",
      "show_filters(w.T, img_shape, (2, 5))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# -- do n_online_loops passes through the data set doing SGD\n",
      "#    This is a good pre-conditioning process prior to L-BFGS\n",
      "online_batch_size = 1\n",
      "n_online_epochs = 4\n",
      "n_batches = n_examples / online_batch_size\n",
      "w, b = autodiff.fmin_sgd(svm, (w, b),\n",
      "            streams={\n",
      "                'xx': x.reshape((n_batches, online_batch_size, x.shape[1])),\n",
      "                'yy': y1.reshape((n_batches, online_batch_size, y1.shape[1]))},\n",
      "            loops=n_online_epochs,\n",
      "            stepsize=0.001,\n",
      "            print_interval=10000,\n",
      "            )\n",
      "show_filters(w.T, img_shape, (2, 5))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# -- L-BFGS optimization of our SVM cost.\n",
      "w, b = autodiff.fmin_l_bfgs_b(svm, (w, b), maxfun=20, m=20, iprint=1)\n",
      "#   -- the output from this command comes from Fortran, so iPython does not see it.\n",
      "#      To monitor progress, look at the terminal from which you launched ipython\n",
      "show_filters(w.T, img_shape, (2, 5))"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "### Exercise 1\n",
      "\n",
      "XXX"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# Write your answer here"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "### Exercise 2\n",
      "\n",
      "XXX"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# Write your answer here"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "### Exercise 3\n",
      "\n",
      "How are the pixel colors encoded in each data set? How are the labels encoded?  Tip: the labels are in `train.y`"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# Write your answer here"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "### Exercise 4\n",
      "\n",
      "The task objects have a `test` attribute as well as the `train` attribute which contains the test set for estimating generalization by cross-validation. How big are the test sets?"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "# Write your answer here"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}