#!/bin/bash

# A script to create a new blog post entry with a predefined template.
#
# Usage:
# ./create-entry.sh "Your New Blog Post Title"

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 \"Your New Blog Post Title\""
  exit 1
fi

TITLE="$1"

# Generate a URL-friendly slug from the title
SLUG=$(echo "$TITLE" | iconv -t ascii//TRANSLIT | sed -r 's/[^a-zA-Z0-9]+/-/g' | sed -r 's/^-+\|-+$//g' | tr '[:upper:]' '[:lower:]')

YEAR=$(date +%Y)
MONTH=$(date +%m)
FULL_DATE=$(date +"%Y-%m-%d %H:%M")

DIR_PATH="content/$YEAR/$MONTH"
FILE_PATH="$DIR_PATH/$SLUG.md"

mkdir -p "$DIR_PATH"

if [ -f "$FILE_PATH" ]; then
  echo "Error: File already exists at $FILE_PATH"
  exit 1
fi

cat > "$FILE_PATH" << EOL
Title: $TITLE
Date: $FULL_DATE
Category: Technology
Tags:
Slug: $SLUG
Author: Jesus Lemus
Summary:
Image: $YEAR/$MONTH/your-image.png
---

Start writing your post here.

## Title 1

some text

> "Important quote, here."
> <footer>— John Doe, Team Topologies</footer>



![A chart showing upward trends in productivity]({static}/images/$YEAR/$MONTH/your-image.png)


Code example
```yaml
# service-template.yaml
apiVersion: v1
kind: Service
metadata:
  name: {{.ServiceName}}
spec:
  replicas: 3
  image: {{.DockerImage}}
  resources:
    # Pre-configured with sane defaults
    limits:
      cpu: "500m"
      memory: "512Mi"
  observability:
    # Monitoring and logging enabled by default
    logging: true
    metrics: true
```

EOL

echo "Successfully created new entry: $FILE_PATH"