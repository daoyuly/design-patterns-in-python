package profile

import (
	"log"
	"math/big"
	"time"
)

func Duration(invocation time.Time, name string) {
	elapsed := time.Since(invocation)
	log.Printf("%s lasted %s", name, elapsed)
}

func main() {
	defer Duration(time.Now(), "p1")
	x := big.NewInt(2)
	y := big.NewInt(1)
	for one := big.NewInt(1); x.Sign() > 0; x.Sub(x, one) {
		y.Mul(x, y)
	}
	log.Println(x.Set(y))
}
