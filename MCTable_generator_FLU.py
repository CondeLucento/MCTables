def flu_latex(frames, sequence):
    n = len(sequence)
    memory = []
    counts = {}

    table = [[""]*n for _ in range(frames)]

    for i, page in enumerate(sequence):
        # ACIERTO
        if page in memory:
            counts[page] += 1
            row = memory.index(page)
            table[row][i] = f"\\acierto{{{page}}}\\flu{{{counts[page]}}}"

        # FALLO
        else:
            if len(memory) < frames:
                memory.append(page)
                row = len(memory) - 1
            else:
                flu_page = min(memory, key=lambda p: counts[p])
                row = memory.index(flu_page)

                del counts[flu_page]
                memory[row] = page

            counts[page] = 1
            table[row][i] = f"\\fallo{{{page}}}\\flu{{{counts[page]}}}"

    # LATEX
    frame_labels = ",".join(str(i) for i in range(frames))
    seq_labels = ",".join(str(x) for x in sequence)

    out = []
    out.append(f"\\fifo{{{frame_labels}}}{{{seq_labels}}}")
    out.append("")

    for r in range(frames):
        fila = "    \\fila{" + "&".join(table[r]) + "}"
        out.append(fila)

    out.append("")
    out.append("\\endfifo")

    return "\n".join(out)

# INPUT
try:
    f_input = int(input("Número de marcos: "))
    s_input = list(map(int, input("Secuencia (separada por espacios): ").split()))

    print("\nCódigo LaTeX generado (Sistema FLU):\n")
    print(flu_latex(f_input, s_input))
except ValueError:
    print("Error: Introduce números válidos.")