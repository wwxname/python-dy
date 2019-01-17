rpc_info = {}


def xmlrpc(in_=(), out=(type(None),)):
    # in_;
    # print(in_)
    # out;
    # print(out)

    def _xmlrpc(function):
        print('注册函数',function.__name__,'参数是：',in_,'输出是：',out)
        rpc_info[function.__name__] = (in_, out)

        def _check_tyes(elements, types):
            print("开始检测入参和出参了")
            if len(elements) != len(types):
                raise TypeError("error")
            typed = enumerate(zip(elements, types))

            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError('arg #%d should be %s'
                                % (index, of_the_right_type))

        def __xmlrpc(*args):

            checkable_args = args[1:]
            _check_tyes(checkable_args, in_)

            print("开始调用自己的函数方法了")
            res = function(*args)
            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_tyes(checkable_res, out)
            return res

        return __xmlrpc

    return _xmlrpc


class RPCView:
    @xmlrpc((int, int))
    def meth1(self, int1, int2):
        print('received %d and %d' % (int1, int2))

    @xmlrpc((str,), (int,))
    def meth2(self, phrase):
        print('received %s' % phrase)
        return 12


print(rpc_info)

RPCView().meth1(1,2)
