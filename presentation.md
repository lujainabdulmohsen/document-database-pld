# Document Databases with MongoDB

## 1. What is this model?
A document database is a non-relational database that stores data as JSON-like documents.

## 2. How is data represented?
MongoDB uses databases, collections, documents, fields and values.

## 3. How do basic operations work?
The POC demonstrates insert, query, update, delete and nested document queries.

## 4. What is this model good at?
- Flexible schemas
- Nested data
- JSON-like data
- Semi-structured data
- Content management
- Product catalogs

## 5. What trade-offs does it introduce?
- Possible duplicated data
- Less strict structure
- Complex relationships may be harder to manage

## 6. How does it compare with relational databases?
Document databases use JSON-like documents and flexible schemas. Relational databases use tables, rows, columns and relationships through keys.

## 7. Where would it fit in a polyglot persistence architecture?
MongoDB can store artwork data, a relational database can store financial transactions, and a key-value database can store sessions and cache.

## POC Demo
1. Connect to MongoDB
2. Insert documents
3. Query documents
4. Query nested fields
5. Update documents
6. Delete documents
