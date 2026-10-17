# Document Database Research Summary

## Introduction
A document database is a non-relational database that stores data as JSON-like documents instead of rows and columns.

MongoDB stores documents inside collections and supports flexible schemas.

## Core Concepts
The main unit of storage is a document. Documents contain fields and values and can include nested documents and arrays.

## Basic Operations
MongoDB supports CRUD operations: Create, Read, Update and Delete.

## Nested Documents
Document databases can store related information inside nested documents. The POC stores artist information inside each artwork document and queries nested fields using dot notation.

## Strengths
- Flexible schemas
- JSON-like data
- Nested data
- Semi-structured data
- Easy integration with modern applications

## Trade-offs
- Possible data duplication
- Less strict structure
- Complex relationships may be easier in relational databases

## Comparison with Relational Databases
Relational databases store data in tables with rows and columns and commonly use primary and foreign keys.

Document databases store related information in JSON-like documents and can reduce the need for joins.

## Comparison with Key-Value Databases
Key-value databases store values using unique keys and are useful for caching and sessions. Document databases allow richer queries on individual document fields.

## Polyglot Persistence
MongoDB can store artwork and artist information, a relational database can store financial transactions, and a key-value database can store sessions and cache.

## Conclusion
MongoDB provides flexible document storage and supports CRUD operations and nested documents.

## References
https://www.mongodb.com/docs/manual/
https://www.mongodb.com/docs/manual/crud/
https://www.mongodb.com/docs/manual/data-modeling/
