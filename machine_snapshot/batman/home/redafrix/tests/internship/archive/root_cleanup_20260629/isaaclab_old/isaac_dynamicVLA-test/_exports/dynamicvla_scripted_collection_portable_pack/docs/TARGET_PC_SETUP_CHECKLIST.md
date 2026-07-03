# Target PC Setup Checklist

1. Install Isaac Sim 4.5.0.
2. Install Isaac Lab 2.2.1.
3. Create a clean project root:
   ```text
   PROJECT_ROOT/
   ├── objects/
   ├── scenes/
   ├── tests/
   ├── datasets/
   ├── datasets-tr/
   └── dynamic-vla/
   ```

4. Download and extract:

   * DOM Testing Set into `tests/` and `test-envs.txt`
   * DOM 3D Objects into `objects/`
   * DOM 3D Scenes into `scenes/`
5. Copy `code/dynamic-vla/` or `code/dynamic-vla-static-v1/` into the project root.
6. Run a tiny headless smoke test:

   ```bash
   -n 1 or -n 3 only
   ```
7. Translate the generated raw data.
8. Generate a multicam video and inspect it.
9. Only scale after the tiny test works.
