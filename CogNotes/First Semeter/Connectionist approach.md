Written by: Laurits Lyngbæk
Source of information: [[Cognitive Psychology (2nd edition) Goldstein, B., & van Hoof, J.C. (2021).pdf|Cognitive Psychology (2nd edition)]]
Association links: [[Knowledge]]
Tags: #📑ChildNode 
___
## Representing concepts in networks: The connectionist approach
Criticism of semantic networks, combined with advances in understanding how information is represented in the brain, led to the emergence of a new approach to explaining how knowledge is represented in the mind.
### The connectionist approach
![Connectionist approach](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Artificial_neural_network.svg/1200px-Artificial_neural_network.svg.png)
>Incoming stimuli, activate the input units, and signals travel through the network, activating the hidden and output units.

Connection weight determines how signals sent from one unit either increase or decrease the activity of the next unit.

```ad-example
title: Activation of output units in a network therefore depends on two things

1) the signal that originates in the input units and 
2) the connection weights throughout the network.
```

#### [[Neural Networks|Connectionist in praxis]]:
![Cannary connectionist](https://slideplayer.com/slide/9365966/28/images/8/The+Rumelhart+Model.jpg) 
> Activation of an item unit ("**canary**") and a relation unit (**can**) causes activity to travel through the network that eventually results in activation of the property units **grow, move, fly and sing, associated with "canary can."**
> 
> (Note that only a few of the units and connections that would be activated by "canary" and can are shown as being activated. In the actual network, **many more units and connections would be activated**.)
> "Rogers, T. T. and McClelland, J. L. (2004). Semantic cognition"

The network is trained when the wrong responses in the property units cause an **error signal** to be sent back through the network, by a process called **back propagation**. Then the weight of the connections in the hidden units are regulated, to not activate fx "a cannary can swim".

```ad-example
title: The following results also support the idea of connectionism

!!! ad-info
	title: Resistant to physiological damage
	Because information In the network is distributed across many units, damage to one part of the brain doesn't destroy memory completly. 
	This theory of **graceful degradation** is simmilar to actual cases of brain damage, in which the brain only looses partial function.

!!! ad-info
	title: Can explain generalization of learning
	Because similar concepts have similar patterns, training a system to recognize the **properties of one **concept also **provides information about other** related concepts.
	This means by learning about canaries, we are able to predict traits about other birds.
```

