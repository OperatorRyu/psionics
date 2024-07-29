import random
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute

def generate_random_number():
    qc = QuantumCircuit(7, 7)
    qc.h(range(7))
    qc.measure(range(7), range(7))

    simulator = Aer.get_backend('qasm_simulator')
    qobj = assemble(transpile(qc, simulator))
    result = execute(qc, simulator).result()
    counts = result.get_counts()

    measured_value = int(list(counts.keys())[0], 2)

    random_number = measured_value % 101
    return random_number

def main():
    correct_numbers = [generate_random_number() for _ in range(20)]
    user_guesses = []
    score = 0

    for i in range(20):
        guess = int(input(f"Round {i + 1}: Guess a number between 0 and 100: "))
        user_guesses.append(guess)
        if guess == correct_numbers[i]:
            score += 1

    print(f"\nYour score: {score}/20")
    incorrect_guesses = [correct_numbers[i] for i in range(20) if user_guesses[i] != correct_numbers[i]]
    print(f"Numbers you guessed incorrectly: {incorrect_guesses}")

if __name__ == "__main__":
    main()
