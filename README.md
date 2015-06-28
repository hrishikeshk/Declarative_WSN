# Declarative_WSN
This is about the design of sensor networks that are defined and implemented following declarative programming paradigms.
The starting point is only to debug and enhance a simple program implementing the shortest path algorithm for a graph/network of sensors.

Added in the directory 'docs' are some background material and the source from where this requirement appears. The paper titled 'Implementation of Declarative Sensor Network' by Yu Du provides the case for using declarative style while writing algorithms dealing with sensor networks. 

First task is to create a simple code for calculating the shortest path in a network. Second should be to benchmark against existing implementation. Finally, extensions in the form of various protocol implementations, such as OSPF among others are expected.

The pyDatalog language (described https://sites.google.com/site/pydatalog/Online-datalog-tutorial) is being used to implement. This includes the entire library support from Python and added facilities to define facts, predicates in the logic programming paradigm.

