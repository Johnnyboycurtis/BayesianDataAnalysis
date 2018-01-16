testx = c(10, 20)
## n = 30

##binom.test(x = 10, n = 30) ## binom.test(x = c(10, 20))

binomialtest  = function(x, n, p = 0.5, 
                         alternative = c("two.sided", "less",  "greater"),
                         conflevel = 0.95
                         ){
  pLower = function(x, alpha){
    if(x == 0){ 0 }
    else qbeta(alpha, x, n - x +1)
  }
  pUpper = function(x, alpha){
    if(x == n) {1}
    else qbeta(1 - alpha, x+1, n-x)
  }
  
  if(length(x) == 2L){
    n = sum(x) ## sum the total values
    x = x[1L] ## first value
  }
  else if(length(x) == 1L){
    if(missing(n)){ stop( "n must be present and n > x") }
  }
  if(alternative == "two.sided"){
   relERROR = 1 + 0.00000001
   d = dbinom(x, n, p)
   m = n*p
   if (x == m){ 
     pval = 1 
   }else if(x < m){
       i = seq.int(from = ceiling(m), to = n)
       y = sum(dbinom(i, n, p) <= d * relERROR)
       pval = pbinom(x, n, p) + pbinom(n - y, n, p, lower.tail = FALSE)
   } else {
       i = seq.int(from = 0, to = floor(m))
       y = sum(dbinom(i, n, p) <= d*relERROR)
       pval = pbinom(y - 1, n, p) + pbinom(x - 1, n, p, lower.tail = FALSE)
   }
   alpha = (1 - conflevel)/2
   CI = c(pLower(x, alpha), pUpper(x, alpha))
  }
  else if(alternative == "less"){
    pval = pbinom(x, n, p)
    CI = c(0, pUpper(x, 1 - conflevel))
  }
  else if(alternative == "greater"){
    pval = pbinom(x - 1, n, p, lower.tail = FALSE)
    CI = c(pLower(x, 1 - conflevel), 1)
  }
  ESTIMATE = x/n
  return(c(ESTIMATE, CI, pval))
}




binomialtest(x = 10, n = 30, p = 0.5, alternative = "greater")
binom.test(x = 10, n = 30, p = 0.5, alternative = "greater")



binomialtest(x = 10, n = 30, p = 0.5, alternative = "less")
binom.test(x = 10, n = 30, p = 0.5, alternative = "less")



binomialtest(x = 10, n = 30, p = 0.5, alternative = "two.sided")
binom.test(x = 10, n = 30, p = 0.5, alternative = "two.sided")


