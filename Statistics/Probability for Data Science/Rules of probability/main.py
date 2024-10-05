# Probability is a branch of mathematics that allows us to quantify uncertainty. In our daily lives, we often use probability to make decisions, even without thinking about it!

# Set theory is a branch of mathematics based around the concept of sets. In simple terms, a set is a collection of things. For example, we can use a set to represent items in a backpack.
# In probability, an experiment is something that produces observation(s) with some level of uncertainty. A sample point is a single possible outcome of an experiment. Finally, a sample space is the set of all possible sample points for an experiment.

# We can’t repeat our random experiment an infinite amount of times (as much FUN as that would be!). However, we can still flip both coins a large number of times. As we flip both coins more and more, the observed proportion of times each event occurs will converge to its true probability. This is called the law of large numbers.


# Rules:

# The union of two sets encompasses any element that exists in either one or both of them. We can represent this visually as a Venn diagram.
# The intersection of two sets encompasses any element that exists in both of the sets.
# Lastly, the complement of a set consists of all possible outcomes outside of the set.



# Independence and Dependence
# The fact that previous coin flips do not affect future ones is called independence. Two events are independent if the occurrence of one event does not affect the probability of the other.

# Are there cases where previous events DO affect the outcome of the next event? Suppose we have a bag of five marbles: two marbles are blue and three marbles are red. If we take one marble out of the bag, what is the probability that the second marble we take out is blue?
# This describes two events that are dependent. The probability of grabbing a blue marble in the second event depends on whether we take out a red or a blue marble in the first event.
# Two events are considered mutually exclusive if they cannot occur at the same time. For example, consider a single coin flip: the events “tails” and “heads” are mutually exclusive because we cannot get both tails and heads on a single flip.


# Addition
# What if we want to know probability of one or both things happening at the same time?
# P(A or B)=P(A)+P(B)−P(A and B)


def prob_a_or_b(a, b, all_possible_outcomes):
    prob_a = len(a) / len(all_possible_outcomes)
    prob_b = len(b) / len(all_possible_outcomes)
    inter = a.intersection(b)
    prob_inter = len(inter) / len(all_possible_outcomes)

    return prob_a + prob_b - prob_inter

# rolling a die once and getting an even number or an odd number
evens = {2, 4, 6}
odds = {1, 3, 5}
all_possible_rolls = {1, 2, 3, 4, 5, 6}
print(prob_a_or_b(evens, odds, all_possible_rolls))

# rolling a die once and getting an odd number or a number greater than 2
odds = {1, 3, 5}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}
print(prob_a_or_b(greater_than_two, odds, all_possible_rolls))

# selecting a diamond card or a face card from a standard deck of cards
diamond_cards = {'ace_diamond', '2_diamond', '3_diamond', '4_diamond', '5_diamond', '6_diamond', '7_diamond', '8_diamond', '9_diamond', '10_diamond', 'jack_diamond', 'queen_diamond', 'king_diamond'}
face_cards = {'jack_diamond', 'jack_spade', 'jack_heart', 'jack_club', 'queen_diamond', 'queen_spade', 'queen_heart', 'queen_club', 'king_diamond', 'king_spade', 'king_heart', 'king_club'}
all_possible_cards = {'ace_diamond', '2_diamond', '3_diamond', '4_diamond', '5_diamond', '6_diamond', '7_diamond', '8_diamond', '9_diamond', '10_diamond', 'jack_diamond', 'queen_diamond', 'king_diamond', 'ace_heart', '2_heart', '3_heart', '4_heart', '5_heart', '6_heart', '7_heart', '8_heart', '9_heart', '10_heart', 'jack_heart', 'queen_heart', 'king_heart', 'ace_spade', '2_spade', '3_spade', '4_spade', '5_spade', '6_spade', '7_spade', '8_spade', '9_spade', '10_spade', 'jack_spade', 'queen_spade', 'king_spade', 'ace_club', '2_club', '3_club', '4_club', '5_club', '6_club', '7_club', '8_club', '9_club', '10_club', 'jack_club', 'queen_club', 'king_club'}
print(prob_a_or_b(diamond_cards, face_cards, all_possible_cards))



# conditional probability measures the probability of one event occurring, given that another one has already occurred.
# Notationally, we denote the word “given” with a vertical line. For example, if we want to represent the probability that we choose a red marble given the first marble is blue, we can write:
# P(Red Second | Blue First)



# Multiplication
# What if we want to calculate the probability that two events happen simultaneously? For two events, A and B, this is P(A and B) or the probability of the intersection of A and B.
# P(A and B)=P(A) * P(B)−P(B or A)