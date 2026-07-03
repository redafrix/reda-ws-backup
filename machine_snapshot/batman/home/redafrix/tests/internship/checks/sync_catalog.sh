#!/bin/bash
set -e

CATALOG_SRC="/home/redafrix/tests/internship/fiper_ws/experiment_catalog/"

echo "Syncing to Bob (pcrobot)..."
rsync -avz --delete "$CATALOG_SRC" pcrobot:"/media/rootalkhatib/My Passport/reda_ws/fiper_ws/experiment_catalog/"

echo "Syncing to Sam (sam)..."
rsync -avz --delete "$CATALOG_SRC" sam:"/home/rootalkhatib/test/reda_ws/fiper_ws/experiment_catalog/"

echo "Syncing to Dean (dean-via-bob)..."
rsync -avz --delete "$CATALOG_SRC" dean-via-bob:"/home/dean/fiper_uncertainty_collection/experiment_catalog/"

echo "SUCCESS: Sync completed successfully to all hosts!"
