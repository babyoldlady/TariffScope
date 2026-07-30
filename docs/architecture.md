# Architecture

FERC API / operator sources -> ingestion service -> database -> search API -> frontend
                                                  -> alerts worker
                                                  -> optional TensorFlow/Vertex AI classifier
