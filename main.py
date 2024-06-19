import numpy as np


def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])

    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)

    diagonalized_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))

    encrypted_vector = np.dot(diagonalized_matrix, message_vector)

    return encrypted_vector


def decrypt_message(encrypted_vector, key_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)

    diagonalized_matrix = np.dot(np.dot(eigenvectors, np.diag(1 / eigenvalues)), np.linalg.inv(eigenvectors))

    decrypted_vector = np.dot(diagonalized_matrix, encrypted_vector)

    decrypted_message = ''.join(chr(int(np.round(np.real(num)))) for num in decrypted_vector)
    return decrypted_message


message = 'Hello, World!'
print("Initial message: ", message)

# make a random key matrix
matrix = np.random.randint(0, 256, (len(message), len(message)))

encrypted_message = encrypt_message(message, matrix)
print("Encrypted Message: \n", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, matrix)
print("Decrypted Message:", decrypted_message)
