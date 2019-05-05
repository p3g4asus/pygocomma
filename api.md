# Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`namespace `[`pygocomma::asyncio_udp`](#namespacepygocomma_1_1asyncio__udp) | taken from https://gist.github.com/vxgmichel/e47bff34b68adb3cf6bd4845c4bed448
`namespace `[`pygocomma::r9`](#namespacepygocomma_1_1r9) | Created on 28 apr 2019

# namespace `pygocomma::asyncio_udp` 

taken from https://gist.github.com/vxgmichel/e47bff34b68adb3cf6bd4845c4bed448
Provide high-level UDP endpoints for asyncio.
Example:
async def main():
    # Create a local UDP enpoint
    local = await open_local_endpoint('localhost', 8888)
    # Create a remote UDP enpoint, pointing to the first one
    remote = await open_remote_endpoint(*local.address)
    # The remote endpoint sends a datagram
    remote.send(b'Hey Hey, My My')
    # The local endpoint receives the datagram, along with the address
    data, address = await local.receive()
    # This prints: Got 'Hey Hey, My My' from 127.0.0.1 port 8888
    print(f"Got {data!r} from {address[0]} port {address[1]}")

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public def `[`open_datagram_endpoint`](#namespacepygocomma_1_1asyncio__udp_1a3921961e515cbed3831a527d48112ce2)`(host,port,* endpoint_factory,remote,** kwargs)`            | Open and return a datagram endpoint.
`public def `[`open_local_endpoint`](#namespacepygocomma_1_1asyncio__udp_1a68d3e9ff398047de73cf9431f2a53632)`(host,port,* queue_size,** kwargs)`            | Open and return a local datagram endpoint.
`public def `[`open_remote_endpoint`](#namespacepygocomma_1_1asyncio__udp_1a2d177040f3c776a1d148825bf05aa2da)`(host,port,* queue_size,** kwargs)`            | Open and return a remote datagram endpoint.
`class `[`pygocomma::asyncio_udp::DatagramEndpointProtocol`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol) | Datagram protocol for the endpoint high-level interface.
`class `[`pygocomma::asyncio_udp::Endpoint`](#classpygocomma_1_1asyncio__udp_1_1_endpoint) | High-level interface for UDP enpoints.

## Members

#### `public def `[`open_datagram_endpoint`](#namespacepygocomma_1_1asyncio__udp_1a3921961e515cbed3831a527d48112ce2)`(host,port,* endpoint_factory,remote,** kwargs)` 

Open and return a datagram endpoint.
The default endpoint factory is the Endpoint class.
The endpoint can be made local or remote using the remote argument.
Extra keyword arguments are forwarded to `loop.create_datagram_endpoint`.

#### `public def `[`open_local_endpoint`](#namespacepygocomma_1_1asyncio__udp_1a68d3e9ff398047de73cf9431f2a53632)`(host,port,* queue_size,** kwargs)` 

Open and return a local datagram endpoint.
An optional queue size arguement can be provided.
Extra keyword arguments are forwarded to `loop.create_datagram_endpoint`.

#### `public def `[`open_remote_endpoint`](#namespacepygocomma_1_1asyncio__udp_1a2d177040f3c776a1d148825bf05aa2da)`(host,port,* queue_size,** kwargs)` 

Open and return a remote datagram endpoint.
An optional queue size arguement can be provided.
Extra keyword arguments are forwarded to `loop.create_datagram_endpoint`.

# class `pygocomma::asyncio_udp::DatagramEndpointProtocol` 

```
class pygocomma::asyncio_udp::DatagramEndpointProtocol
  : public DatagramProtocol
```  

Datagram protocol for the endpoint high-level interface.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public def `[`__init__`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1aff877b5974826c7864e197c5f6b9bfe5)`(self,endpoint)` | 
`public def `[`connection_made`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1a3f6a65ad683aefada05d44040379274d)`(self,transport)` | 
`public def `[`connection_lost`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1ac882788a94f1bb68923e12c94a8d8147)`(self,exc)` | 
`public def `[`datagram_received`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1a8395213d125851b65b6a85790966549c)`(self,data,addr)` | 
`public def `[`error_received`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1ab290f6ba3236d0b0b6cad1e9bdb669e2)`(self,exc)` | 

## Members

#### `public def `[`__init__`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1aff877b5974826c7864e197c5f6b9bfe5)`(self,endpoint)` 

#### `public def `[`connection_made`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1a3f6a65ad683aefada05d44040379274d)`(self,transport)` 

#### `public def `[`connection_lost`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1ac882788a94f1bb68923e12c94a8d8147)`(self,exc)` 

#### `public def `[`datagram_received`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1a8395213d125851b65b6a85790966549c)`(self,data,addr)` 

#### `public def `[`error_received`](#classpygocomma_1_1asyncio__udp_1_1_datagram_endpoint_protocol_1ab290f6ba3236d0b0b6cad1e9bdb669e2)`(self,exc)` 

# class `pygocomma::asyncio_udp::Endpoint` 

High-level interface for UDP enpoints.
Can either be local or remote.
It is initialized with an optional queue size for the incoming datagrams.

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public  `[`broadcast`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1ad7bf74c266ab407a946f9eaeed2fe819) | 
`public def `[`__init__`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a62f4d46052f9dd78e42f9a2728fe6eb0)`(self,queue_size)` | 
`public def `[`feed_datagram`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a33de1ed0076a4108fe059af35bbda35b)`(self,data,addr)` | 
`public def `[`close`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1adf8f98237ad3d1002558af1c23108ca3)`(self)` | 
`public def `[`protocol`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a7b7eaade98a46cbc4cf92edb6e147e32)`(self,data,addr,check_data_fun,timeout,retry,is_broadcast)` | 
`public def `[`broadcast`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a48f4d9e3a6943f78e9688323c2bc555d)`(self)` | 
`public def `[`broadcast`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1aa0ad3596c9fc568dd5f83367344f9bef)`(self,v)` | 
`public def `[`send`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a997f48e9fd9637ba33c6cb5b802a0223)`(self,data,addr,expect_response)` | Send a datagram to the given address.
`public def `[`receive`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1ac3a8d8937a6db3035ffb15040e392163)`(self,expected_sender)` | Wait for an incoming datagram and return it with
`public def `[`abort`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a5dc8e679534f03598dc1b3dfa36caa07)`(self)` | Close the transport immediately.
`public def `[`address`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1acf83fbbd850ffb7d932133969c6f488a)`(self)` | The endpoint address as a (host, port) tuple.
`public def `[`closed`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1ac459f80a9b96235facb67f2cb07f3719)`(self)` | Indicates whether the endpoint is closed or not.

## Members

#### `public  `[`broadcast`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1ad7bf74c266ab407a946f9eaeed2fe819) 

#### `public def `[`__init__`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a62f4d46052f9dd78e42f9a2728fe6eb0)`(self,queue_size)` 

#### `public def `[`feed_datagram`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a33de1ed0076a4108fe059af35bbda35b)`(self,data,addr)` 

#### `public def `[`close`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1adf8f98237ad3d1002558af1c23108ca3)`(self)` 

#### `public def `[`protocol`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a7b7eaade98a46cbc4cf92edb6e147e32)`(self,data,addr,check_data_fun,timeout,retry,is_broadcast)` 

#### `public def `[`broadcast`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a48f4d9e3a6943f78e9688323c2bc555d)`(self)` 

#### `public def `[`broadcast`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1aa0ad3596c9fc568dd5f83367344f9bef)`(self,v)` 

#### `public def `[`send`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a997f48e9fd9637ba33c6cb5b802a0223)`(self,data,addr,expect_response)` 

Send a datagram to the given address.

#### `public def `[`receive`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1ac3a8d8937a6db3035ffb15040e392163)`(self,expected_sender)` 

Wait for an incoming datagram and return it with
the corresponding address.
This method is a coroutine.

#### `public def `[`abort`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1a5dc8e679534f03598dc1b3dfa36caa07)`(self)` 

Close the transport immediately.

#### `public def `[`address`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1acf83fbbd850ffb7d932133969c6f488a)`(self)` 

The endpoint address as a (host, port) tuple.

#### `public def `[`closed`](#classpygocomma_1_1asyncio__udp_1_1_endpoint_1ac459f80a9b96235facb67f2cb07f3719)`(self)` 

Indicates whether the endpoint is closed or not.

# namespace `pygocomma::r9` 

Created on 28 apr 2019

@author: Matteo

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public def `[`testFake`](#namespacepygocomma_1_1r9_1a94b60d082becd4ea067d2e08a0929e6d)`(n)`            | 
`class `[`pygocomma::r9::R9`](#classpygocomma_1_1r9_1_1_r9) | 

## Members

#### `public def `[`testFake`](#namespacepygocomma_1_1r9_1a94b60d082becd4ea067d2e08a0929e6d)`(n)` 

# class `pygocomma::r9::R9` 

## Summary

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public def `[`__init__`](#classpygocomma_1_1r9_1_1_r9_1afcf149690b694c65bfeb20b49193b75f)`(self,hp,idv,key,timeout,force_reconnect_s)` | Costructs R9 remote Object.
`public def `[`__repr__`](#classpygocomma_1_1r9_1_1_r9_1a6a0e598e53be629a41b1296514cd5324)`(self)` | Gets string representation of this R9 object.
`public def `[`destroy_connection`](#classpygocomma_1_1r9_1_1_r9_1a3cab2178523dfa8d3c66a2af01b90d8c)`(self)` | Destroys the connection with the R9 device.
`public def `[`ask_last`](#classpygocomma_1_1r9_1_1_r9_1a7d21a233927822a2f85addc4b8c64a97)`(self,timeout,retry)` | Sends ping to R9 object to get last command.
`public def `[`ping`](#classpygocomma_1_1r9_1_1_r9_1ae9be1fbd653c8e9ebcfb9ae57bb38c76)`(self,timeout,retry)` | Sends ping to R9 object to see if it is online.
`public def `[`emit_ir`](#classpygocomma_1_1r9_1_1_r9_1a2c15053436aede8bb0f773ff8fc2f466)`(self,keybytes,timeout,retry)` | Sends ir to the R9 device.
`public def `[`enter_learning_mode`](#classpygocomma_1_1r9_1_1_r9_1afaadcc2775e723da22defa5f143e76b4)`(self,timeout,retry)` | Puts R9 in learning mode.
`public def `[`exit_learning_mode`](#classpygocomma_1_1r9_1_1_r9_1a01677f9b8581c807965cc1a8b117cd0d)`(self,timeout,retry)` | Exits R9 learning mode.
`public def `[`get_learned_key`](#classpygocomma_1_1r9_1_1_r9_1a9262375eb161f435d245f8a370a24110)`(self,timeout)` | Puts R9 in learning mode.

## Members

#### `public def `[`__init__`](#classpygocomma_1_1r9_1_1_r9_1afcf149690b694c65bfeb20b49193b75f)`(self,hp,idv,key,timeout,force_reconnect_s)` 

Costructs R9 remote Object.

#### Parameters
* `hp` [tuple] A tuple with host and port of the R9 remote

* `idv` [string] id of the R9 object

* `key` [string|bytes] key used to encrypt/decrypt messages from/to R9

* `timeout` [int] timeout to be used in TCP communication (optional)

* `force_reconnect_s` [int] seconds after which to force reconnection

#### `public def `[`__repr__`](#classpygocomma_1_1r9_1_1_r9_1a6a0e598e53be629a41b1296514cd5324)`(self)` 

Gets string representation of this R9 object.

#### Returns
[string] string representation of this R9 object

#### `public def `[`destroy_connection`](#classpygocomma_1_1r9_1_1_r9_1a3cab2178523dfa8d3c66a2af01b90d8c)`(self)` 

Destroys the connection with the R9 device.

#### `public def `[`ask_last`](#classpygocomma_1_1r9_1_1_r9_1a7d21a233927822a2f85addc4b8c64a97)`(self,timeout,retry)` 

Sends ping to R9 object to get last command.

This command is sent not crypted

#### Parameters
* `timeout` [int] timeout to be used in TCP communication (optional). If not specified, the timeout specified when constructing the R9 object will be used

* `retry` [int] Number of retries to make if no device is found (optional)

#### Returns
[dict|NoneType] On successful send, the decoded confirmation dict obtained by R9 device is returned. Otherwise return value is None

#### `public def `[`ping`](#classpygocomma_1_1r9_1_1_r9_1ae9be1fbd653c8e9ebcfb9ae57bb38c76)`(self,timeout,retry)` 

Sends ping to R9 object to see if it is online.

#### Parameters
* `timeout` [int] timeout to be used in TCP communication (optional). If not specified, the timeout specified when constructing the R9 object will be used

* `retry` [int] Number of retries to make if no device is found (optional)

#### Returns
[bytes|NoneType] On successful send, bytes got from R9 are returned; None otherwise.

#### `public def `[`emit_ir`](#classpygocomma_1_1r9_1_1_r9_1a2c15053436aede8bb0f773ff8fc2f466)`(self,keybytes,timeout,retry)` 

Sends ir to the R9 device.

#### Parameters
* `keybytes` [bytes] key to be emitted by R9 device. The key should be a byte object that represents lirc/arduino format array of little-endian shorts. This is the same format obtained with the learning process

* `timeout` [int] timeout to be used in TCP communication (optional). If not specified, the timeout specified when constructing the R9 object will be used

* `retry` [int] Number of retries to make if no device is found (optional)

#### Returns
[bytes|NoneType] On successful send, the array of bytes obtained by R9 device is returned. Otherwise return value is None

#### `public def `[`enter_learning_mode`](#classpygocomma_1_1r9_1_1_r9_1afaadcc2775e723da22defa5f143e76b4)`(self,timeout,retry)` 

Puts R9 in learning mode.

#### Parameters
* `timeout` [int] timeout to be used in TCP communication (optional). If not specified, the timeout specified when constructing the R9 object will be used

* `retry` [int] Number of retries to make if no device is found (optional)

#### Returns
[dict|NoneType] On successful send, the decoded confirmation dict obtained by R9 device is returned. Otherwise return value is None

#### `public def `[`exit_learning_mode`](#classpygocomma_1_1r9_1_1_r9_1a01677f9b8581c807965cc1a8b117cd0d)`(self,timeout,retry)` 

Exits R9 learning mode.

#### Parameters
* `timeout` [int] timeout to be used in TCP communication (optional). If not specified, the timeout specified when constructing the R9 object will be used

* `retry` [int] Number of retries to make if no device is found (optional)

#### Returns
[dict|NoneType] On successful send, the decoded confirmation dict obtained by R9 device is returned. Otherwise return value is None

#### `public def `[`get_learned_key`](#classpygocomma_1_1r9_1_1_r9_1a9262375eb161f435d245f8a370a24110)`(self,timeout)` 

Puts R9 in learning mode.

#### Parameters
* `timeout` [int] timeout to be used in TCP communication (optional). Default value is 30 seconds. If awaited, this method will block until a key is not received or timeout seconds have been passed

#### Returns
[bytes|NoneType] On successful key reception, the byte object representing the learned key is returned. this can be used with emit_ir function for future key sending. It returns None on error or on timeout (no key was pressed/detected)

Generated by [Moxygen](https://sourcey.com/moxygen)