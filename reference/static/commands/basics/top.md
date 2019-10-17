top

`top` is a command that allows users to see information about their CPU and memory usage.

<!-- one line explanation would go here -->

<!-- minimal example -->

```bash
$ top

Processes: .....
Load Avg: .....
SharedLibs: .....
MemRegions: .....
PhysMem: .....
VM: .....
Networks: .....
Disks: .....

PID     COMMAND    %CPU     TIME        TH      WQ      PORT        MEM     ......
...     ...        ...      ...         ...     ...     ...         ...
...     ...        ...      ...         ...     ...     ...         ...
...     ...        ...      ...         ...     ...     ...         ...

```

---

### Useful Options / Examples

#### `top -pid *processId*`

```bash
$ top -pid 90702
Processes: .....
Load Avg: .....
SharedLibs: .....
PhysMem: .....
VM: .....
Networks: .....
```

##### Break it down

-   The `-pid` option asks `top` to only display a monitor of only processes
    with the specific process id
-   The would be useful if you want to easily see information about a
    specific application that is open on your device (i.e. how much physical
    memory is used by Google Chrome)

#### `SPACE` (within the minitor)

##### Break it down

-   The CPU/Memory monitor periodically updates with the most recent information
-   Pressing `SPACE` when inside the CPU/Memory monitor immediately updates it

#### `q` (within the minitor)

##### Break it down

-   Exits the CPU/Memory monitor immediately
