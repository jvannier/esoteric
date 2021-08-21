[
    Comments. Even valid characters ('<', '>', '+', '-', ',', '.')
        are ignored as the current cell is 0, so the loop is never
        called.
]

[
H  a  p   p   y      F  a  t   h   e   r   '  s      D  a  y   !     I     l   o   v   e      y   o   u   ,     D  a  d   .
72 97 112 112 121 32 70 97 116 104 101 114 39 115 32 68 97 121 33 32 73 32 108 111 118 101 32 121 111 117 44 32 68 97 100 46

Cell 0 && 1 == Loop counters
]

++ # Cell 0 = 1
>+++++ # Cell 1 = 5
[
    <++++++ # Cell 0 plus 6
    >- # Until Cell 1 is 0
]
< # Move to Cell 0

# Cell 0 = 32 === smallest ascii character
[
    >++ # H
    >+++ # a
    >+++ # p
    >+++ # p
    >+++ # y
    >+ #
    >++ # F
    >+++ # a
    >+++ # t
    >+++ # h
    >+++ # e
    >+++ # r
    >+ # appostraphe
    >+++ # s
    >+ #
    >++ # D
    >+++ # a
    >+++ # y
    >+ # !
    >+ #
    >++ # I
    >+ #
    >+++ # l
    >+++ # o
    >+++ # v
    >+++ # e
    >+ #
    >+++ # y
    >+++ # o
    >+++ # u
    >+ # period
    >+ #
    >++ # D
    >+++ # a
    >+++ # d
    >+ # period
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
]

+++++ # Cell 0
[
    >+ # H
    > # a
    >+++ # p
    >+++ # p
    >+++++ # y
    > #
    >+ # F
    > # a
    >++++ # t
    >+ # h
    >+ # e
    >+++ # r
    >+ # appostraphe
    >+++ # s
    > #
    > # D
    > # a
    >+++++ # y
    > # !
    > #
    >+ # I
    > #
    >++ # l
    >+++ # o
    >++++ # v
    >+ # e
    > #
    >+++++ # y
    >+++ # o
    >++++ # u
    >++ # comma
    > #
    > # D
    > # a
    > # d
    >++ # period
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
]

++ # Cell 0
[
    >+ # H
    >>>>>>>> # appy Fat
    >+ # h # Index 10
    > # e
    >+ # r
    >+ # appostraphe
    >++ # s # Index 14
    > #
    >++ # D
    >>>> # ay !
    >++ # I
    > #
    >+ # l # Index 23
    > # o
    >+ # v
    >>>>> # e you
    >+ # comma # Index 31
    > #
    >++ # D
    > # a
    >++ # d
    >++ # period
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<-
]

[
H  a  p   p   y      F  a  t   h   e   r   '  s      D  a  y   !     I     l   o   v   e      y   o   u   ,     D  a  d   .
72 97 112 112 121 32 70 97 116 104 101 114 39 115 32 68 97 121 33 32 73 32 108 111 118 101 32 121 111 117 44 32 68 97 100 46
]

>+ # H
>+ # a
>+ # p
>+ # p
>> # y
>+ # F
>+ # a
> # t
>+ # h
> # e
>+ # r
>>>> # appostraphe s D
>+ # a
> # y
>+ # !
>>>>>>>>>> # I love yo
>+ # u
>>> # comma D
>+ # a
> # d
> # period
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< # Get back to Cell 1

z

.>.>.>.>.>
.>.>.>.>.>
.>.>.>.>.>
.>.>.>.>.>
.>.>.>.>.>
.>.>.>.>.>
.>.>.>.>.>
.>.
