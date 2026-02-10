def count_plural_nouns(nouns):
    """
    Count the number of plural nouns in a list.
    
    Args:
        nouns: List of noun strings
        
    Returns:
        Integer count of plural nouns
    """
    plural_count = 0
    
    for noun in nouns:
        if noun.endswith(('s', 'es', 'ies', 'ves')):
            plural_count += 1
    
    return plural_count


# Example usage
if __name__ == "__main__":
    nouns_list = ["cat", "dogs", "box", "boxes", "baby", "babies", "wolf", "wolves"]
    
    result = count_plural_nouns(nouns_list)
    print(f"Plural nouns found: {result}")
