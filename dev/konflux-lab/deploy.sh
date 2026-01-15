#!/bin/bash

# הגדרת ה-Namespace הרצוי
EXPECTED_NS="idankatz-dev"

# קבלת ה-Namespace הנוכחי שבו הטרמינל נמצא
CURRENT_NS=$(oc project -q)

echo "--- Pre-deployment Check ---"

# בדיקה: האם אנחנו ב-Namespace הנכון?
if [ "$CURRENT_NS" != "$EXPECTED_NS" ]; then
    echo "ERROR: You are currently in namespace '$CURRENT_NS'."
    echo "This script is intended for '$EXPECTED_NS'."
    echo "Please switch using: oc project $EXPECTED_NS"
    exit 1
fi

echo "Confirmed: Running in $EXPECTED_NS. Starting deployment..."
echo "------------------------------------------------------"

# עדכון המשאבים
echo "Applying Tekton Tasks..."
oc apply -f tekton/tasks/

echo "Applying Tekton Pipelines..."
oc apply -f tekton/pipelines/

echo "------------------------------------------------------"
echo "Success! Resources are updated."
echo "To run the pipeline, use: oc create -f tekton/runs/idan-pipelinerun.yaml"
