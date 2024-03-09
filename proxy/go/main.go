package proxy_pattern

import "fmt"

// IObject to use proxy and to object they must implement same methods
type IObject interface {
	ObjDo(action string)
}

// Object represent real objects which proxy will delegate data
type Object struct {
	action string
}

// ObjDo implement IObject interface and handel's all logic
func (obj *Object) ObjDo(action string) {
	fmt.Printf("I am real Object ObjDo. I can, %s", action)
}

// ProxyObject represent proxy object with intercept action
type ProxyObject struct {
	object *Object
}

// ObjDo are implement IObject and intercept action before send into real object.
func (proxy *ProxyObject) ObjDo(action string) {
	if proxy != nil {
		proxy.object = new(Object)
	}
	fmt.Printf("I am in proxy object. intercept %s", action)
	if action == "Run" {
		proxy.object.ObjDo(action)
	}
}
