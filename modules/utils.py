def sliding_window_transcript(transcript, max_tokens, overlap_tokens):
    """
    Splits the transcript into overlapping chunks.

    Args:
        transcript (str): The full transcript text.
        max_tokens (int): Maximum number of tokens per chunk.
        overlap_tokens (int): Number of overlapping tokens between chunks.

    Returns:
        list: A list of overlapping transcript chunks.
    """
    tokens = transcript.split()  # Assuming space-separated tokens for simplicity
    chunks = []
    start = 0

    while start < len(tokens):
        end = start + max_tokens
        chunk = tokens[start:end]
        chunks.append(' '.join(chunk))
        start += max_tokens - overlap_tokens

    return chunks
