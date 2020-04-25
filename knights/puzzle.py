from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    #A is a knight or a knave but not both
    Implication(AKnight,And(AKnight,AKnave))
    #If A was a knight then the statement must be true 
    )

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),
    #If A is Knave then A lies so both A and B cannot be knaves 
    #If A and B both are not Knaves then A lies so it is a knave
    Biconditional(AKnave,Not(And(AKnave,BKnave)))
    
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Or(BKnight,BKnave),
    Not(And(BKnight,BKnave)),
    # If A is a knight then both are of same type
    Biconditional(AKnight,Or(And(AKnight,BKnight),And(AKnave,BKnave))),
    #If b is knight then both are of different types
    Biconditional(BKnight,Or(And(AKnight,BKnave),And(AKnave,BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    #If B is knight then he speaks the truth-A said 'I am knave'
    #Here if A is knight it has lied and if it is a knave it has spoken the truth
    #which means A is both a knight and a knave
    Biconditional(BKnight,And(AKnight,AKnave)),
    #If B is knave he has lied i.e A is not both knight and knave
    Biconditional(BKnave,Not(And(AKnight,AKnave))),
    Biconditional(BKnight,CKnave),
    Biconditional(BKnave,CKnight),
    Biconditional(CKnight,AKnight),
    Biconditional(CKnave,AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
