
### Fundamentals of Embedding Vectors and Their Role in RAG Systems

- Embedding vectors transform words, phrases, or entire documents into numerical representations within a high-dimensional space. 
	- In this space, semantical/related concepts are positioned close together, while unrelated ideas are placed far apart.

### Embeddings in Vector Space

- Embeddings are often described as the bridge between raw data and LLMs, because they translate unstructured human language into a structured numerical form that machines can process.
- Embeddings are coordinates that locate meaning in a shared semantic space enabling machines to measure similarity.

### Traditional and Modern Embedding Methods

#### TF-IDF
- Term Frequency - Inverse Document Frequency
- *Term Frequency* - counts how often a term appears in a document.
- *Inverse Document Frequency* - reduces the weight of very common words that appear across many documents.
	- If a word appears in 2 out of 100 documents, its IDF is high.
	- If it appears in all 100, its IDF is very low.
- TF-IDF score is TF multiplied by IDF.
	- High score - word is frequent in the given document, rare across the corpus; thus, more informative.
	- Low score - word is either rare in the document or common everywhere; less useful.
- Text as sparse vectors of word frequencies weighted by rarity
- Simple, fast, good for keyword-based search
- Ignores word order and context, cannot capture semantic meaning
#### Word2Vec
- Analyzes large amounts of text; captures the semantic meaning of words
- Dense vector representations of words, contexts in large corpora
- Captures semantic relationships
- Low-dimensional dense vectors
- Similarity between words
- Static embedding
- Limited to handle longer text
#### Embedding Models
- Transformer architecture
	- Input embeddings - raw text is tokenized; each token is mapped to a dense vector
	- Positional encodings - allows the model to note the order of words
	- Self-attention mechanism - each token looks at all other tokens in the sequence and decides how much attention to give them
		- Multi-head attention - instead of one attention calculation, multiple heads run in parallel, each focusing on different types of relationships
	- Feed-forward neural network
	- Output layer
- Attention mechanism
- Text is converted to numerical representations
- Importance of a component in a sequence relative to other components
- Contextualized vectors
- Execellent for semantic search, question answering, RAG
- Long documents, relationships across sentences
- Computationally expensive, large pre-trained models

### Embedding Vectors for Retrieval and Generation

- Three steps
	- Semantic search
	- Similarity matching
	- Relevance ranking
- User submits a query, it's converted into an embedding, and the system compares the embedding with the embeddings of stored knowledge. The pipeline can then identify documents or passages that are semantically related. The pipeline can then return an LLM response with the necessary context provided.
- Common metrics include:
	- Cosine similarity: measuring angle closeness
	- Euclidean distance: allows the system to rank candidate documents not by keyword overlap, but by conceptual similarity
- Relevance ranking
	- Higher vector similarity ensures that the most relevant information is surfaced first.
- Challenges
	- Vector Quality
		- Poorly trained embeddings fail to capture semantic relationships
		- Domain mismatch
		- Granularity matters
		- Benchmarking against real tasks
	- Storage and Scalability
		- Storage requirements grow quickly
		- Specialized vector databases
	- Updating Embeddings
		- Model updated, stored embeddings no longer compatible
		- Dynamic data requires periodic re-embedding
		- Versioning strategies
		- Quality, scalability, maintainability
	- Vector Drift
		- Embedding model is updated or fine-tuned, producing vectors no longer aligned with older ones
		- Queries no longer match previously indexed documents
		- Problematic in long-lived systems
	- Large-Scale Storage
		- Millions or billions of embeddings
		- Storage footprint grows rapidly
		- Challenge of efficient retrieval
		- Specialized vector databases
		- Approximate Nearest Neighbor (ANN)
	- Updating Outdated Knowledge
		- Remain current
		- Embeddings are static
		- Outdated embeddings = stale information
		- Re-embedding new documents
		- Operational challenges

### Optimizing and Evaluating Embeddings to Improve Performance

- Quality assurance
- Performance measurement
- Optimization

### Why Not All Embeddings Are Equally Effective
- Domain mismatch
- Task dependence
- Representation limits

#### Intrinsic Evaluation
- Word similarity tests: model's embedding systems are compared to human judgment
- Analogy tasks
- Clustering and visualization: examining whether embeddings naturally group related words together

#### Extrinsic Evaluation
- Search relevance: retrieving the right documents
- Classification accuracy
- Question answering performance
- Task-driven perspective

#### Similarity Metrics
- Closeness in vector space
- Cosine similarity: Measures the angle between two vectors, focusing on orientation rather than magnitude; captures semantic similarity very well
- Euclidean distance: Measures the straight line distance between vectors; more sensitive to vector magnitude
- Dot product: Used for efficiency, though combines magnitude and orientation, which may not always reflect semantic closeness

#### Source of Bias
- Embeddings learned from large text corpora
- Stereotypes, offensive associations, cultural imbalances
- Impact
	- Search and ranking: may retrieve or prioritize irrelevant, harmful results
	- Downstream LLM responses: generated output enhances biases
	- Fairness and trust
- Data Curation
	- Clean, balanced, diverse corpora
	- Filter out toxic, biased, or underrepresented language
- Model Choice & Fine-tuning
	- Models trained with fairness considerations
	- Fine-tune embeddings on domain-specific data
- 