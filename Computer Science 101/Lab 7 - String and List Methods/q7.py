sentence = input("Please enter a sentence: ");

individual_words = sentence.split();
no_repeated_words = [];

for item in individual_words:
    if(item not in no_repeated_words):
        no_repeated_words.append(item);
        
no_repeated_words = no_repeated_words[::-1];
mapped = ", ".join(no_repeated_words);

print(f"Unique words: {mapped}");
