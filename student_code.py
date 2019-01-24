import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if isinstance(fact, Fact): #check if it's an instance of fact
            if (fact.name is "fact"): #checking if it is a fact/ double check
                for x in self.facts:
                        if (x == fact): #if the fact is already in the kb
                            print("The fact has already been asserted.")
                self.facts.append(fact) #add new fact to the kb
        else:
            return #ignore if its not a fact
    
        """
        elif (fact.name is "rule"): #checking if it is a rule instead
            for x in self.rules:
                if (x == fact): #if the rule is already in the kb
                    print("The rule has already been asserted.")
            self.rules.append(fact) #add new rule to the kb
            """

        print("Asserting {!r}".format(fact))
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))

        #make sure the Fact is a fact
        
        things = ListOfBindings()
        for x in self.facts:
            y = match(x.statement, fact.statement) #check to see if the fact statement matches any statements in the kb
            
            if (y): #add to the list of bindings if the match returns bindings
                things.add_bindings(y)
        if (things): #if things contains bindings, return them
            return things
        else:
            return False #if there is no fact in the kb, return false
        
