#lang racket
; Team TuRNeR : Tina Nguyen, Rayat Roy
; SoftDev pd1
; K27 -- Basic functions in JavaScript
; 2022-02-03

(define fact
  (lambda (n)
    (if (= n 0)
        1
        (* (fact(- n 1)) n)
        )
    )
  )

(define fib
  (lambda (n)
    (if (= n 0)
        0
        (if (= n 1)
            1
            (+(fib(- n 1)) (fib(- n 2)))
            )
        )
    )
  )

(fib 10)
(fact 3)