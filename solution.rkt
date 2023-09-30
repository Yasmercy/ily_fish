(define k 100)
(define g 9.81)
(define m 0.2)
(define t 0.5)
(define fs 0.1)
(define fk 0.05)

; iter up
(define (a1 x0) (/ k 2))
(define (b1 x0) (- (- (* m g (sin t)) (* fk m g (cos t)))))
(define (c1 x0) (- (* x0 m g (sin t)) (/ (* k x0 x0) 2) (- (* x0 fk m g (cos t)))))
; iter down
(define (a2 x0) (/ k 2))
(define (b2 x0) (- (+ (* fk m g (cos t)) (* m g (sin t)))))
(define (c2 x0) (- (* x0 m g (sin t)) (/ (* k x0 x0) -2) (* x0 fk m g (cos t))))

; driver function
(define (xf x0)
  (display x0)
  (cond 
    ((< x0 (/ (+ (* fk m g (cos t)) (* m g (sin t))) k)) 
     (xf (/ (+ (- (b1 x0)) (sqrt (- (* (b1 x0) (b1 x0)) (* 4 (a1 x0) (c1 x0)))) (* 2 (a1 x0))))))
    ((> x0 (/ (- (* fk m g (cos t)) (* m g (sin t))) k)) 
     (xf (/ (- (- (b2 x0)) (sqrt (- (* (b2 x0) (b2 x0)) (* 4 (a2 x0) (c2 x0)))) (* 2 (a2 x0))))))
    (else x0)))
