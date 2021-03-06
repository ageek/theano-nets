#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Example using the theanets package for learning the XOR relation.'''

import lmj.cli
import numpy as np
import theanets

lmj.cli.enable_default_logging()

X = np.array([
               [0.0, 0.0],
               [0.0, 1.0],
               [1.0, 0.0],
               [1.0, 1.0],
             ])

Y = np.array([0, 1, 1, 0, ])

Xi = np.random.randint(0, 2, size=(256, 2))
train = [
    Xi + 0.1 * np.random.randn(*Xi.shape).astype('f'),
    (Xi[:, 0] ^ Xi[:, 1])[:, None]]

e = theanets.Experiment(theanets.Regressor,
                        layers=(2, 2, 1),
                        learning_rate=0.1,
                        learning_rate_decay=0,
                        momentum=0.9,
                        patience=300,
                        num_updates=1000)
e.run(train, train)


print "Input:"
print X

print "XOR output"
print Y

print "NN XOR predictions"
print e.network.predict(X)


