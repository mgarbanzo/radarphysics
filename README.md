radarphysics
============

Radar tools for Physical Applications

There is a problem with this file:
/usr/lib/python2.7/dist-packages/numpy/lib/function_base.py
in the line 1971 the double should be complex if a complex signal is passed.
If this change is not done, it will produce inadecuate frequencies,
giving a false spectrum.
