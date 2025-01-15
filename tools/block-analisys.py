import base64
import json
import sys

# Sample JSON block
block_data = {
    "jsonrpc": "2.0",
    "id": -1,
    "result": {
        "block_id": {
            "hash": "0F213DDBF77783C639FB8166C175B39FBBDA806FFB12D6FBFE7469662B1CF825",
            "parts": {
                "total": 1,
                "hash": "D4501A95B31C264CF25F851B67ADCE0D9D498884422C3B86544DC6F811A32EAE"
            }
        },
        "block": {
            "header": {
                "version": {"block": "11"},
                "chain_id": "juno-1",
                "height": "23070494",
                "time": "2025-01-15T08:45:13.467702041Z",
                "last_block_id": {
                    "hash": "8DFA22CB468F1AF03DB67054235A927347642C143E1513396683B24448DB4C33",
                    "parts": {
                        "total": 1,
                        "hash": "5C245ACE9D2117ACD6580CB8E62575AF858A4D1E96EC47CD7B3F7EB2948DA757"
                    }
                },
                "last_commit_hash": "1A2DE65E7D89024A1CEF65EA0FEE554530E8034A866411C6CCAB45CAE7B82355",
                "data_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
                "validators_hash": "442ACB49E5EC2398AAB2DB07467D1F53CF15CD508D9BDE1B6C746363F24FBBBB",
                "next_validators_hash": "442ACB49E5EC2398AAB2DB07467D1F53CF15CD508D9BDE1B6C746363F24FBBBB",
                "consensus_hash": "1BF2556CA5D5D7EFFB540F34CB0FFC77A3202E32275557AFBD219882A9E42ACF",
                "app_hash": "85861E1E347DBDEA69F21CF11B09396235DB5FC2AA083CFEC18D141E64411221",
                "last_results_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
                "evidence_hash": "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
                "proposer_address": "1470B9237056641663CB4DFDEC86B064578B29BF"
            },
            "data": {"txs": []},
            "evidence": {"evidence": []},
            "last_commit": {
                "height": "23070493",
                "round": 0,
                "block_id": {
                    "hash": "8DFA22CB468F1AF03DB67054235A927347642C143E1513396683B24448DB4C33",
                    "parts": {
                        "total": 1,
                        "hash": "5C245ACE9D2117ACD6580CB8E62575AF858A4D1E96EC47CD7B3F7EB2948DA757"
                    }
                },
                "signatures": [
                    {
                        "block_id_flag": 2,
                        "validator_address": "80F24BFDA3E6A8C1BAC0517E7665AC9145D609F7",
                        "timestamp": "2025-01-15T08:45:13.477546532Z",
                        "signature": "mPBaL/3DRg1uoM6+nMnNpiTFKWOG7zOYAz72zM3s47obp5QHzak86KBikJoVWhavf34UviZV7hbX7owcG2eZCg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "980644C9C8033945BA54EF32C053C395D0269EEA",
                        "timestamp": "2025-01-15T08:45:13.425665109Z",
                        "signature": "JXUtSROcb5xrWjJZZxWsrbUci/IOtl5VU18ljPGXnpzsBtLQOXLVV8GqW6v/1AdHSkVSpJKHUd13My2AuHQ5Cg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "1470B9237056641663CB4DFDEC86B064578B29BF",
                        "timestamp": "2025-01-15T08:45:13.525211591Z",
                        "signature": "cLA9S2+4fXHc+tXwNNo8dW+DN7ZU+YP2702xhqbR9oejVpYwDSNjPrPuymelA5DbQJfyRP6Ad8QYKK2KkAjrAA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "0F1ED70645D475745565C702588BD1EEBA62C28B",
                        "timestamp": "2025-01-15T08:45:13.462553235Z",
                        "signature": "duWfYkVV5lWZ3+8GaDewMRQAz8NvB9JCY5xRC5RYrffJ4rywPiIqj3VfzGpQp5sHm+5apHo907ERXvXc6x1GCA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "F9D7C618E5E46C3B942EC35BCC8145BA3DB8423F",
                        "timestamp": "2025-01-15T08:45:13.498696352Z",
                        "signature": "o3n/CxZipzzFm9aGO8T3A6r64A00Hq7N6lhobdG9Kno4BkBEsz2N+83aRILLs0flDUkOWwSpz5CX+RrHf/TEAg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "31E927F677282369B7E57D39FF9C47E3845BFDEA",
                        "timestamp": "2025-01-15T08:45:13.467702041Z",
                        "signature": "AyU7dWEwiS6BWrSWn/dxiNonT/L006a9mbFYssgPlF0XSVq3En/TjpKhEv9anb1F24Y7T7H8gZ+nZyCuQ04QCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "1B431E63CC50C7BA283AC9E2F0A13FDD1FC86F74",
                        "timestamp": "2025-01-15T08:45:13.433025444Z",
                        "signature": "g5kA1X23hUOoP1KLrHKtBLgaARSqXxkIrTdMhBPAJH7Oq50vY8ZLq+W6vZ2cmeLThdvhYGK0njwUTt6VJOEaDQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "26DD4D34B61136958ED2E7E0BE710291417F77E9",
                        "timestamp": "2025-01-15T08:45:13.536577124Z",
                        "signature": "Zk04GPgqhLYZQM1xpmGv9qlh8RU2L/sHaYw2DsUaDQSbgl+YcX47YP+xtLkM+nx24u4g6xYwwY9M/iJNWibBBQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "D971748C41BD4B777502DCABE903A71A3669A77A",
                        "timestamp": "2025-01-15T08:45:13.447988625Z",
                        "signature": "nFuzip/HtoIRfpjHu6lDu+rLSY3yWFf8v3KSNbuKkWOZ6AsP6vQeb7jCAMeguTZsYkfmSgTqE6ExYF/1NFXXCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "FCF0C1EAE20E3C808B4C3E5112AA49AE01C60F8C",
                        "timestamp": "2025-01-15T08:45:13.513241645Z",
                        "signature": "DRznsyCCTn/iL9OV1WIp71JQGCt8SXpSxw7Q1cWTYS8yKtdmgmO327cFldeQA/Hnlb7E8aBW80dnDRm+O2dRBQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "011CA32A120D5F8007BE9D2AA60C1C7AE8F02634",
                        "timestamp": "2025-01-15T08:45:13.465737183Z",
                        "signature": "RSlSXergjkuemIlhVf7e905d8DnVxUkTuXuNI7pN2TA4rD5b5UscfEx0PoscTaaC2cKYI2YExwI0WZ0oPPeZBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "3876144FE42DD069E414F648A9FA2C933D4939DF",
                        "timestamp": "2025-01-15T08:45:13.436606888Z",
                        "signature": "T2hQoRIbF1hGKIvR1qLXD//XCDI/SCxMrMd06PM+idAiOO1dQtnFIlG5wunuI8h0tayFkrN0+jkWopBKoz0PBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "A50CF609192A6CF1C6835D56274D18B30459425E",
                        "timestamp": "2025-01-15T08:45:13.459919362Z",
                        "signature": "BqF5/m4C0w5ZmrKgICbJq+Wvrf9PGQ5hgxaIErbuv2CKeQFd12nrHOS7e+rU2Phfu11zNT04G8NcFWSZ4qdZCA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "FDA77E3592437D1B06EEF7F858363587A38E1D12",
                        "timestamp": "2025-01-15T08:45:13.477119143Z",
                        "signature": "woK1zvGtVYqsiVh+2rSKaPhpzKUm0fItv3haT9LCdsUxy33CYBRX+yVXYXx+VmM1obrjk3koyxx9Hi7wfsDgBw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "8B68344DC158475291B2AC6B668E931A77BAFDA4",
                        "timestamp": "2025-01-15T08:45:13.486093141Z",
                        "signature": "+sGBhGs1aG+jQX86P9E+okoHtX5S2BrJG/3NERAcVnHCj7VxUV8I635uLczZaZIj12jcP12fFehhzkxdoeHGBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "6678356FBEC44F52259BC8711B35400F440FC8EB",
                        "timestamp": "2025-01-15T08:45:13.482273095Z",
                        "signature": "/N5VZzDmUFNFOh/boqiXSjdvaT53ga+8dsdraLfIIl8vHKGw4DXY0IY08yJ98gfNx9SzRQnxduzHCz4EzeHrCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "6D2B3AC0DEC4412CA87714E1F1B1BEE882E62F5A",
                        "timestamp": "2025-01-15T08:45:13.467440239Z",
                        "signature": "SqjZVReYdDG65Zl/Rqh4KXwQ89Syz9p+oUpKdGXNxdebrCELHYzAdPLqZwEctW26X0HxFd2ZJlRUWjS7BDPVDQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "4947683341BA5ED2E583032F237AF51E9FB98E82",
                        "timestamp": "2025-01-15T08:45:13.588897016Z",
                        "signature": "uBQzHfY5cGUz/gCZCSX4B/DUFToomLWjBtt/A8RminsgMh/omr0EYuOh+1eWPlLQorh+zVNkA8MupgZem1SxBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "B57D60F0B3E0F9548D1C60385D46584356DD61DC",
                        "timestamp": "2025-01-15T08:45:13.455323498Z",
                        "signature": "Jz0f9/3LkhjhYkTnL5t44IMcPZmAzzBFLxEepdRyS+lzrJq99F7Pv3k3mVB1cTj1IGXH3hMzMlU0WyvGGNbNDA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "970C896E7C2CE31811E2BC784167108AFC1F44B0",
                        "timestamp": "2025-01-15T08:45:13.449206272Z",
                        "signature": "wbGZNk0O5LrMbn68fi/6hrotGQEaHKTVTGOXrmrK/bg0JQ+HQXvlA7/d//TWI9Zt3syoE/isQZsAilWzZguUBw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "687E9D3B8DBC07E22DBA8A8FABBD1E7C51EB48C6",
                        "timestamp": "2025-01-15T08:45:13.429963833Z",
                        "signature": "SK9WHLo7rcHYC+Ucj5y6r0/VnuuvMBzt0o2e36vk6qLS+02s95eRpwiU+ZDFQHQaOG3agGcxok45wp/d+ifZCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "CB8E49AB7CC1F4F17E79B2C14D31A9C0EE8ABBA6",
                        "timestamp": "2025-01-15T08:45:13.408157599Z",
                        "signature": "VToXK9wiB/OiKCgyBNiWw49lO5OAJ5WyYumSlC+rTHtQYrxNlwhnVtH+ObsoScku8kFdlnhk3IaOBXwXuD1EDw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "B2F50E82D354517E17E37178A0D4A8A9644C4D4D",
                        "timestamp": "2025-01-15T08:45:13.512469601Z",
                        "signature": "CwRHF9moC0YK7jlrDAUCgb66Qt3Sm1IoExXo9bbWZJi7+VR/K5Q28qSVCo9BpEbtEtfCbgNbwXJbcfoI3n5lBQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "9945C4BCA1EFAD0E461EB84D79CC283130AD569E",
                        "timestamp": "2025-01-15T08:45:13.433230421Z",
                        "signature": "6w7bmx96oPAyDKn3R2Ry3czfV8WQl4/nVm7rGXhqZFdApFaDl+5ZQ1nvYQKhlW4gmNcYLE0xgJoOJwumuDqsAg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "EF5DC39DD40EFF73A2ACD4318812CAFF2EAAA2A9",
                        "timestamp": "2025-01-15T08:45:13.554322267Z",
                        "signature": "+R0zkTIsF6IPj7in2CYb+7LzWxaphdNCcqinyZjjUh91WLVDgRFfdG0zxDcqiRIiWhT5rFKazTd5G2SUEsxxDQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "33E7D788A563CF87FA86AA63817A198A43364EDE",
                        "timestamp": "2025-01-15T08:45:13.512225979Z",
                        "signature": "U9/4aojVN93OZegjrxSYbRBda8vxmrh8u0rdbZnyQ/r4ANW3jEe6H9NEnPKjO5KBuIUL3FFomMWIBl9Js5pMCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "FDA22C79E4C93CBEACD0297036F7650839D6223D",
                        "timestamp": "2025-01-15T08:45:13.438721951Z",
                        "signature": "gqDVManVD3hmmg3GXydM/MryYmKuoqX6lyLL9PfZ/gSGI2Vvn5sp0e/jpiT2DIofLT803Il5aynIh6q/GJR0Bw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "64B93D226FD19BFFE48A802ED742D1DC427693EF",
                        "timestamp": "2025-01-15T08:45:13.538381726Z",
                        "signature": "rAjajPcdAnnZI7AF1haup4uIn8lWKrf1RyWaFpSoxN67PrE3rzP/JrpoCDUJ3kCprBGrzwvx4L5kRIitZyyXAw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "05F1DCE023B7415274B8400D7D8B95AE95E625F3",
                        "timestamp": "2025-01-15T08:45:13.420149098Z",
                        "signature": "Ld9M/XbX9C9l50b02ixYmGiIR/VHw0Ov2/XgfKjHq8In2dLpq/6WK64f8nh0GC7C8+YZMVcytEcejQ8z50ZyDg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "596CC5372AC7DF5E8F80D4F73F84A1B3E835EA6A",
                        "timestamp": "2025-01-15T08:45:13.544980418Z",
                        "signature": "9WSrMoW2G0YCp9rUTQEo4S+rAxoaWUCLLNZcNoQP+vTq+AWuoGSNiAyOjVtanRQMkODKCu3ubHjQB5NqYUyqBg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "CE7B52696BC06193E36BFB10E6CC0A3561D837D4",
                        "timestamp": "2025-01-15T08:45:13.51168489Z",
                        "signature": "+vvS4bRI3wPslAp/CvrQpr86DC+Qq7AKFLOEAi2DIjA0GVw/uPvsHf9MU178nq2viCjwsbbwY6z9uplyYzMcBQ=="
                    },
                    {
                        "block_id_flag": 1,
                        "validator_address": "",
                        "timestamp": "0001-01-01T00:00:00Z",
                        "signature": ""
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "FEE0233B3771EAEB26617E367138A0A6EFAA79B1",
                        "timestamp": "2025-01-15T08:45:13.442031563Z",
                        "signature": "U3Wb+NcrppcQYgQMtvnwyTpnE/QvmB4Sk4sw7sTxe5dBoCGpLbTY3hYGOY5WiqbThIhH71WMwEdGQuk9/lSFDQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "376258981B5C8270319BE5CD655C628903DC41C1",
                        "timestamp": "2025-01-15T08:45:13.447040316Z",
                        "signature": "yd8iO76v0ztMPrbhu+a9+j5FcvgYjcnCo4y6J9lfcJClp/VBfm/K6abxPBWWLcJ6+Mu9Pw5vdF8M+2eh+1LxDw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "B67DDDDF3392C5980B4E0868CC1770BE9118FE65",
                        "timestamp": "2025-01-15T08:45:13.466152141Z",
                        "signature": "NqT8vRhEWWPnVW9P2GsqBPjX8Nyc/nKIfFkWfzNo+AM6bHGgtJIlotnLzDUdt4YhlBBC3Fbdiz5QyONCAloeDg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "B1AF1820ADDDB6F06C6B76BF46C86A98CA88D244",
                        "timestamp": "2025-01-15T08:45:13.434199067Z",
                        "signature": "x/JJtBKcBCPxxgigzHivenReHFIvlvDwnL2J1YVq5ITIy9OBRQrgOInVytjbyYpNcgnokM882I7Z4sBbty67AQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "126D191091FFB0C205CEDE35AA71896B54C2E0F0",
                        "timestamp": "2025-01-15T08:45:13.498133147Z",
                        "signature": "mQJDM8qqcJGrq21pbuSu5Bz3SUkXGD0uPCh9jzEV59acAYF2HMpCXVRUKm/hSBJ3gCOspUEMlVGrvdJ2cJdQCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "D8D80BD5D6D758C3014374AA8EEC545F46686151",
                        "timestamp": "2025-01-15T08:45:13.427671571Z",
                        "signature": "/DcNfQVTkrzmON2mExrjjhpvyNvGOgzKMzEBj4gPgADxdRiDSJ4xHKCSUa9QSP6JLcY2WNGvOCvJWFK5am84AA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "7992AB6A4A94EB3EE9D5D3E6E4129D2F0AF5D2D3",
                        "timestamp": "2025-01-15T08:45:10.529188484Z",
                        "signature": "rfdI7jgeb+U3vHahfuRHLtmjeB3DLuQUceJtGeK3wSxaxaRsK0Fiz7DMol8qSGfuIaixk07vKDzJTMTYBzK6DA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "891B7D6D28C39786EA4FF974231D3856EB3E27F6",
                        "timestamp": "2025-01-15T08:45:13.424091352Z",
                        "signature": "vHnSOQs3HZnit4VdmeCyATXKtVseo2sOmuWPT3JY0fF1lEmNqxLGVGM2Ve1H9YEMFx3mk92H8E6nVz4eXa8JCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "D226E146E35E3097E53C09147F5F6E89E4C83EFF",
                        "timestamp": "2025-01-15T08:45:13.436610567Z",
                        "signature": "T9tGSm69z/FJxjuJYAqPiPtN+NsWMBrLapwx27Ig+1nO0UB2+nyHwHzNS2DDA+0lo9QGLykxSA8ulvflGYPfAQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "7BC6768A0B45EC84A40AC8EC013B1ED022D5E303",
                        "timestamp": "2025-01-15T08:45:13.465041448Z",
                        "signature": "nUW/47B+YvrCq3QsW1PYQ9qmExf3aejeWUg/fS7W60FCx7pTy+V6FD9BtXH5ZD96ipgLcwslCLauH/TdYBilAw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "042CA91A597C492082FEFCE5D022035F106C71EB",
                        "timestamp": "2025-01-15T08:45:13.465919384Z",
                        "signature": "xoLG7PP0fd8Je/HJ+l2yGErNXe+MSKzGKJqjoXJhC1uZyndhVusHVC6+pKIkRZoseVvBHircvpgQyjyXkUWeAA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "A3F728A1BEF2B4860A7B8104C9CE56ACFFC85561",
                        "timestamp": "2025-01-15T08:45:13.442105831Z",
                        "signature": "rWEIgTMhHZ8FKjAofOjK4E3Xp5jFyk0/EGveQWrOEpCLPdeoovsR30drqAgYbiA3kzO38WpxGX7RjRpT2sw9Dg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "E85369365EFAF2003506117F8BEC27AD5B03D4A6",
                        "timestamp": "2025-01-15T08:45:13.4893475Z",
                        "signature": "CTgfdK4+EtIfUWXDfxIAefSFoXt7XVe4vRcK7W2tl4Sn8+DjXMXNzgMVOfC7VBJ3+j7JIL4dSLqj3JGJH9X0BA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "A318B3EA83A87531C2BE401173FE60954E0E4D5F",
                        "timestamp": "2025-01-15T08:45:13.537795992Z",
                        "signature": "5vFKIyaslpz7OxiHIqCsADjWOOrCOBA106CYH1oFdUmvCwsCprIlqydFh7dbjmydetqBG0PBiQKrmczCk4HvCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "EE5E6EE4DA40A30F18BC1EE052AC4F9C84D35F00",
                        "timestamp": "2025-01-15T08:45:13.502728535Z",
                        "signature": "6NqMuTwq/o707vRNMhVQQoBP1KCTqp7uetzQ80fTZWwNh/C6YcxJD0iZIlA03vFDkNLeVt4l13LFzgYbZEkjAA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "09C809054D9CCEDB5594CBFC96CFFA053D7DD02E",
                        "timestamp": "2025-01-15T08:45:13.489106326Z",
                        "signature": "3OOaMDT2dGPpExNaCJ/qgBOmAXM8QrODi2xsFewGYD9adDCGNDC9V23wads7fVRxgwE0550+BObn609J0vMoDA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "706AED795780D65B06127B2CB7BF08961116C9FF",
                        "timestamp": "2025-01-15T08:45:13.494133988Z",
                        "signature": "GXJuCGvT7F90xwcSekitVKlk3sUUmNF/jPbSSSNEbmgTnwD5gKerTZkCTqtpNNsIZcDH8YqSM9IdwFEVWk7dCg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "FCB482F4E0111DF6C85DB7099B473608ED67248F",
                        "timestamp": "2025-01-15T08:45:13.461036762Z",
                        "signature": "EoL056dMK95FWsFPKONVVlwad8/HYoavuO8lnuT3bdMzjLsisJWIAAcAKP8BIPzYrdxPXdpuBAfE04UX1BeUBQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "BF480EF88DB244A6DEFC6EF6C739720124CB8AFE",
                        "timestamp": "2025-01-15T08:45:13.674042571Z",
                        "signature": "jLr32tNChBcxSZ61UL8xzDWnQhVJoFKy0bOS0qW4or8D6GcqkDbwJW+CmuO5Duy8l4XOT+Dh4My9QGXP35k3Bg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "26C5A7EFCD9F11ED7E846F7EC63DEF2D5A55969D",
                        "timestamp": "2025-01-15T08:45:13.607376115Z",
                        "signature": "eCjBqvqkoQcNY26HxdLJkMyeP7YdiJ0kkbeqUKkQJuLHiBfeBREdWS4x6ovM1oihgGObolcBOXaV9m64+JI7Dg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "E04A7742ACD0163004B664A703B7920488A2AE86",
                        "timestamp": "2025-01-15T08:45:13.431527858Z",
                        "signature": "cSBtCUQPsTMPj3zZISGr3wfES3YTBRQAIApuxUEszUBHhb7h2wodSBaC5ByHR67oOLAPPu3sO882s1FIvW8NCw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "640B7E370FE54961870389E2BE27F616E72CDB16",
                        "timestamp": "2025-01-15T08:45:13.539441134Z",
                        "signature": "fAgOjJrS591qEMISONaWJdv5iDNqi9Xc8WbtKX+9203e34MxSHSfbqeEEgxg3B1ufyZaRKeHuHzC4Oj8FbzmCw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "D2C08B4DB6CC564701FA562DA96E54F04BE5857C",
                        "timestamp": "2025-01-15T08:45:13.545523694Z",
                        "signature": "TT2Ethh8TwxzVpc9MNEhDTn/sTVNVQjTrSqH4bp9kzyYUw8Y3PKVLkpmHLzXXottP+0DdRBMISz30FCHudBtAA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "0CE325E2DDFD572A20C834017B933008195596E9",
                        "timestamp": "2025-01-15T08:45:13.4637296Z",
                        "signature": "Bz0RQoXrj0OrY/w2Nka8k66Z9b+Ckkxf+KP8q1vBX1xtxwb78z7ej2q2EUgM/+F5zK0n0vgUBwQoLhPrCwszAA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "C0CA289D913689AC0A9450375E4208F473FD5A2D",
                        "timestamp": "2025-01-15T08:45:13.438506364Z",
                        "signature": "afpjBTjpcibAFo9jagzLFaE5PugMGNppCsdWxMwqFEWS8dxDBlTL49nAqMD/jDmCCU+FX4SFwwz7KZFy55jlAg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "0855A780C7EABDAB44FC31341278D7B41ED9CE96",
                        "timestamp": "2025-01-15T08:45:13.706796038Z",
                        "signature": "fDmdGy8B+xqfPO77CJs8KKWZ+uQUVJ3kZKpUqTezZNYqx0wrnI9I6Cjq3UIhY3meMPIagO+KE1L5iDGGOE23CQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "8E7A970AB8AEF7B361B01BBD730285C5D4EFD30F",
                        "timestamp": "2025-01-15T08:45:13.53148689Z",
                        "signature": "o8v7+bmnEbNFGbbo+coaWi22HUR1SRzobQR5q4x0mx4erTSX7+4xv6lN+bftpu3V4GM5xa4vDInym0I8vBWyAA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "554CC1217B3BA242C5F3BD11DC377C2800147EA5",
                        "timestamp": "2025-01-15T08:45:13.514167757Z",
                        "signature": "4K9tGp8o4kAgSZl5nPwoKtSYLN1bGtorU0Q6BAHhn44gcbGerV6lRxhMiV03VOLFvderskWIxYCvqQTbOX5CBw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "EAB33CDAD8D5B57DB5BCD0F176CB9D170A6DA200",
                        "timestamp": "2025-01-15T08:45:13.44934511Z",
                        "signature": "7vRNMNvD2pDukBbPo70dshbClkXR57vzgU9um9Ccr0hkQRcj3eTxDbj1mu7khtrXmUXkcdkABcNBJknM7KPaAQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "149825C294B6936AD8833F5F2055AFD64B6E260F",
                        "timestamp": "2025-01-15T08:45:13.546885017Z",
                        "signature": "2PsgwCQsATrecEA5/EiWJMFCSanlCPeb2Z9wNYnzdhzBcHPKMGLfSDU4hVOLed4iINEtkpuIgldl9TUt+nsWCw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "2A8023A1977E7C521107502B803AEC57FFAA6094",
                        "timestamp": "2025-01-15T08:45:13.490153378Z",
                        "signature": "xkoWKYzpLckD9xM0NVNU8PUakzNyuHghTVq0W43ECO9MWPamnirQ8TY3se1xwKN71gSmnZVa5yWmZnWinBTgCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "3E1DEB86DB0748495A5C7D0E3D89AEDB68BDBD32",
                        "timestamp": "2025-01-15T08:45:13.509820821Z",
                        "signature": "ufi1Cm/rbsmHQ2X/gBV74oay8ZJFgVUd1jPkHx2KnkLi/2YDp1fnZL/u09fCjWcCzd0la/+wP3lxtGVwnrRXCg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "1A0FB0B119DD4A7606EAA5ACE96C59A8EDA70734",
                        "timestamp": "2025-01-15T08:45:13.455822502Z",
                        "signature": "sEGKyRa7EKEgXIhhwEVdbdvaJvK9aTU2cEplioMKbtBUdUleTupIiq82dtXZyq6xlAS1UuKAVKw2CMhvLLWGAw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "895AE6DEA762125D1D3EA62735CE28F4079448A3",
                        "timestamp": "2025-01-15T08:45:13.462437643Z",
                        "signature": "Rca/e9fzs11/iDh1MEewJ1WyGT1aXrwKkXbEmAC4mhb0NTVu8sWmzrzcPyhX6JGBelE9hKqJt/k3XHrAJCp5DQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "7926DCCFF4CD77DD8F842BB79FB96679C1635AF4",
                        "timestamp": "2025-01-15T08:45:13.445238019Z",
                        "signature": "VSFui0KGT0jTcNEm2t+zleKIR2hx56dhPcGR2qzoH0eWORd2SMfMloNzgRu4+C1LFfg349FD9c8Y78tiXbVlAw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "A758F131985687FE5F72DEC968B96C21C20DC93D",
                        "timestamp": "2025-01-15T08:45:13.463316405Z",
                        "signature": "pqkfhkw1jy5d/vIBBnM9XT9Kpb/nZKGPwG5qAwt3m+zab0MlQu2rJFbJmKvrBWTeJM50hpRJMqrJtY9hGCYDCw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "3D680F8EF25FCF01FCD24957C665E8F23D07EA66",
                        "timestamp": "2025-01-15T08:45:13.448650366Z",
                        "signature": "NwevzFBqO3IuGfo52JttT3/Puk7JlZ+M78ulTgWFgrKf0L91jndvWEnLTbUZT/BBoQCOZihXiaGb6YD2EBNuBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "175DF90C23CDAB4965DBE0433AF7E850FAF9E4DC",
                        "timestamp": "2025-01-15T08:45:13.419438291Z",
                        "signature": "R2hJwNdm0hZKQzpY5xEmzOaBKvhA8tghbqSex8eICqFTNannc2QykoqZNpKsMHp6RNzuKQpr0JWk0jji/FMCAg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "DDDE88D0B6E9ECCB109037704E35592B243FFE2B",
                        "timestamp": "2025-01-15T08:45:13.641852155Z",
                        "signature": "FUwKQ0pz+QPowLzfULRQvWw6FOPcORn9GAoq5ZByDUTbYrsx+uPJfjk2IbhK8z0bGGNu/VbSM7Bjtb5WSSw7Bw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "ED5A383F89D74B59E040E1D33E78C9EF5323FD53",
                        "timestamp": "2025-01-15T08:45:13.475093921Z",
                        "signature": "nftCLC347uQB92DfBJRUrUxSn/LhrQfnGF1i+8ixj4B7RKPHVHCKFHLzFlSXZNx0oaSm5q/Jwe149tPhORhuAQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "A19F8CA134065BDBC764D53A5A024F091F8D58F0",
                        "timestamp": "2025-01-15T08:45:13.539371264Z",
                        "signature": "UbfXARqX6NyAEFaloitTaV3fjD52WeAl7Enjtkzm94n7m+2aL4PpG6z9p1sM8W7PDnWWKsKsz8hoJ8r0DXB6BQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "10DED706EFAE3E176E39559EB9927AC30DB1F0E8",
                        "timestamp": "2025-01-15T08:45:13.45834084Z",
                        "signature": "eEgWa1SsRgfm3NfcB/Z8DcjAZRt4Ksj/igtwqQrn2ZhlcE0Vz0l6hFgwwdXTGR7G/bZJ6FrJZ50I8/c89yuyDw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "82594A20244F29C881CDE573F82D7A334BB54770",
                        "timestamp": "2025-01-15T08:45:13.536620199Z",
                        "signature": "Jq/GNjx0oQ9XV9qU2hlj1zwqDg7V6rMEqAikIi/Rgqrf3k/lO4lLvf8fi8cHximVsFnxT0bCbwaK5KW2UNV7Cg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "30795CFA451DE58B6B4F7A34FC73AFF9ED16CAE0",
                        "timestamp": "2025-01-15T08:45:13.434225684Z",
                        "signature": "42cyABVDelYj1W20O407/mykcocNb/mZKiqtc5Xla+jj28Tdpei3zy9ADli07h6dwIvyNBrtCgs7wWM7fnDoCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "560F1B2786B4B854C756B49ABCED9AC4A26B7FFF",
                        "timestamp": "2025-01-15T08:45:13.605744038Z",
                        "signature": "QC+mcu9f27o8IKxOwuJk7XXdrqHxtzKjZJiyhh6ZHftYCjOv6y1u+bKlPPqpq4ezYfT0RAudAT9byyqDG4sJBg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "154B35F02A0881E71F45CDDC4AA46FD310E20812",
                        "timestamp": "2025-01-15T08:45:13.512827796Z",
                        "signature": "oEcAM1twC7nyOz4PFwTJ6x5D/TxWTU/GSfVvmP+X2beYUdUbiL/KsDBvH63TuwLsN4LQDWDTtdOJ+dWIGVe4CA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "CEE07615BB3D2467E0982E9F6EEBCB4197AF041E",
                        "timestamp": "2025-01-15T08:45:13.561592171Z",
                        "signature": "OgLQEmG98melJxbKEMvVrrkPseIWGs2paxMJZHspRKXEKCDnBgcucrQOvCiNMXm1h2okMQIkPULGTgf0jzGTCw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "EBAAECF31EC18DC4234E01C82B749AE2CD7A9577",
                        "timestamp": "2025-01-15T08:45:13.487938287Z",
                        "signature": "P1N8s8fO92G/YprOJyfoWrrIAPEUZmk9mZEVJ6IF/ih/1x8g2jPP1vTBapB3Ns4dGh5hKZisM85sx3bgaGygDg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "83F286870F6AD40171663EAB308ADA7770550EBC",
                        "timestamp": "2025-01-15T08:45:13.487049485Z",
                        "signature": "Pdt8U1XKGohMNbf7qdBtn42kgaFneJvcr+ELZvGuIACAP0F/NhNV61niRG7xrOOkr7EjK9mOh0XHJuhATwJIBg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "21F2E30ECC6F02B6BDCDF7B50F6CA8C28D527AE8",
                        "timestamp": "2025-01-15T08:45:13.445614546Z",
                        "signature": "3mCt0g0o/VOsWn0DqdtKWkhqXzAyAjjWhTksFoWGEFokARWJQfzTyyhAOfuZ5jFn2hUSAalf1vV+BclT7rc7Bw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "87EB79967FEE5FC636AF59391AB5B6DA6E5FF253",
                        "timestamp": "2025-01-15T08:45:13.445990205Z",
                        "signature": "w00FfeY84ZbU2m+810kfX2HZm1aXg7sZYZpmQsH/uv+bKHG7EBx189NAT1alQNHoVv9QIOooZ2U997RGHSpEAA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "45226E6BC30DBEC14D0242ADADDC9110C4581D72",
                        "timestamp": "2025-01-15T08:45:13.446113379Z",
                        "signature": "37AzOy2QmNh7f3sUma8E8pSny34Q+tvZfRxhMCob+3FRJmfJJgJA+tKTEDVtqbFOeTl9uQa78v45vvNyBTcRAg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "FEFE87FF0E1766CA5788EF4FFD56DD218DD55299",
                        "timestamp": "2025-01-15T08:45:13.54235918Z",
                        "signature": "L+z4pWfy+5u57BU/Ln2jBGpvytpfy/fUOJtHWcAdoWZPUZnXzm160D5rr7bcoEMUKaZokjwFxMcYpsOpOrVcDg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "D87730AAF169362894C9EA7AA423B96D1EA957D9",
                        "timestamp": "2025-01-15T08:45:13.43300324Z",
                        "signature": "3/3m9K1nq90gSALj0bdxs98oghyJ6PUGYCcWhc2Zk3OtPbkqMTQ5gtRnfZQaVJg9wldF3EJzkpi2LCTXM5MZDA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "F4C65C2B8D8BD96037652F375E789E2EEA4305DB",
                        "timestamp": "2025-01-15T08:45:13.53395013Z",
                        "signature": "fVjd1RRc7dI4+EqV+MnmdU0dvyeeCRp5OC2JisOS/kwowzphRJaJVvGkZ4vlYb6rb08BoeNSvDAeteOwQ54zBQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "42706A040AB648A3D298025AEAB6B82F80A152D8",
                        "timestamp": "2025-01-15T08:45:13.427694765Z",
                        "signature": "i1MP5SoQuBEfSr8A9wLkjW+lZP7WV+JAP/zjEnz+9KS6GPbHWvqrGM20kUZMgtpL63GEXKv65QpCIeSweq2KBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "15BBFCA9F07F8AD7D40D657157C3E7F824C02C25",
                        "timestamp": "2025-01-15T08:45:13.426810519Z",
                        "signature": "AfZ6jcU99Fv9CyohXVaquYLnvkScfiUkYYjDlZrY+XJ3Al7+gASe19OBfAZXzxpvtAAaAQg65CLthjOLs+KsCg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "AF9408C088DB1E7ADA52A764C5645B792C977825",
                        "timestamp": "2025-01-15T08:45:13.517564966Z",
                        "signature": "pSq3fd6SkvIAUM2LZ41jrZiGdhH5HEuIFHUEoDvwht5h7d5PgKvOqrGPe9zfSlGuESdSt4J+30CuMYAuly5FAQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "7F530838B75FD46D07133BFAE4383AA2123C96A2",
                        "timestamp": "2025-01-15T08:45:13.443523337Z",
                        "signature": "JD1slR65fg8SDLjjF9ywXB0aaOhPKI9HPOPds8PKyD+ENWIcRpzevAWou0+FrY5e/MkmM76oV/Zf0sqLyFmfDg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "E3A16135F74AC8A2F3DE70E62BC6B94F1BD2E316",
                        "timestamp": "2025-01-15T08:45:13.464140825Z",
                        "signature": "vav7iw04PF2M9U3npSAA1EvrBS+h9kHjWJHAR7iSPIyRVOa/UcpavIaG3diGJdPhThNroWQ3SyfZ+iiOVMyfBw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "468F19774D884937ECAC184F1704B280A52684C5",
                        "timestamp": "2025-01-15T08:45:13.513729767Z",
                        "signature": "8jM1i/n12elVaVqgIGh51/EfmGzY+E8ozFj3RWlgjiZ26UUnAJydu91sJsUbF8lf/nfLbpNq0kK7DaLaDhirBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "F81AF64A49D9FCF0AC5ABA9676B84E71CCDC7623",
                        "timestamp": "2025-01-15T08:45:13.514414176Z",
                        "signature": "Ay5uOr5vz3Xsp3gEmKHrTTbhIpJc1y/a5BzpVbCHhSkyu2jINaegxiM9bfle8Dy8n5ydI5gRNtdezBZ9YFQ+Ag=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "5D0C8C47492C7B5806C6A0AEC2B61A22BABDF304",
                        "timestamp": "2025-01-15T08:45:13.610383142Z",
                        "signature": "Zne/FfI6Lpf1p3ehiVBr/LmBtuC7smb4QQG2weUIoB/nj0Pm8ytEKMTWrnc3SfZVqJDU/5JpKH5pPW37lNSdBw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "D88899651B0E78D95A01B696D616584AB2A17836",
                        "timestamp": "2025-01-15T08:45:13.429865933Z",
                        "signature": "ceIh3E5CU4DjQpUwhH3czXIP2lyDqXp/DS3GYRMuhNujzBz1CVP4T9inIve6iMlPgwbBLIPgxWyH8F5SCzk9BA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "7990B032D89DB6DFB2368B09BB961D1E1BB932DA",
                        "timestamp": "2025-01-15T08:45:13.624311799Z",
                        "signature": "Ksp1L7mhDzbH3RLIvYGmb4ApPquAMWTNCC+P5+83cMwECaH3pSmKtFHM955+9KUW2SejA6TnidMbxKYmi/yYCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "72C874A2BC59B8E3316DDE995CB9368E79529A3E",
                        "timestamp": "2025-01-15T08:45:13.536152804Z",
                        "signature": "ne1ESOHA/CGna4NZac3O2DiJCtqUsa1cVEZLuUFqvx8ebIIlSSQFj72TvNhGQ4JAiQQ9BetyTKALNT1nMN+kBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "CABF6F72DF30E58B6193C7F2250FB99F3510393C",
                        "timestamp": "2025-01-15T08:45:13.532364217Z",
                        "signature": "U5aH5eGvJjccneydieK6HudRH/qrZeigAYGtwDWXYognCZVxsqtkMRUsh3/f+U6LIxdg1kLijRAHwuMCnUaqAA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "D24AA323EF77312855D4266F6D40723514733C89",
                        "timestamp": "2025-01-15T08:45:13.566581063Z",
                        "signature": "XO3WFrtvAV6FU++DjtNX9Udl13U+jfDAuddu8qsUXeeXhFiIsfIgsNgM/mCxk90hUvZiMBxrGQXlaNfxpuZGDQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "4E6F0443575D135BFC7E036E95D00A79CBECB023",
                        "timestamp": "2025-01-15T08:45:13.745032019Z",
                        "signature": "X/OAU/vf+ENQ1ENp+mfsnbNx1O2N7+3k9phMLT23whZm6KF9U5pY6jG+6FAEdojmXeoU3JzNctM5/lxdJxXTBQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "1FF354C5F1F9112F7EF36642369861814B85ECEA",
                        "timestamp": "2025-01-15T08:45:13.433694072Z",
                        "signature": "7HvL9Nbo0y7LTLqF2Nw7RzH1qJOSdR6LmaHn6wczgQ9efH0hVFRl9xAI0mZ5GA/D3qIjZ+0Z8qbb034sXtZiAw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "8D56A016414356DD90C35D88E68465BA5E41FAD1",
                        "timestamp": "2025-01-15T08:45:13.436870902Z",
                        "signature": "T0pZcW6YoZV3KffsWovwFhAelCBU/k1goKLsaMhRRd8an2NaGgxrIUorPxhpTFE4qhVdDxOrnrtZd1PKyCIKCA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "2586F90EE50AFDB92FBEB01A026E66FAFD00096D",
                        "timestamp": "2025-01-15T08:45:13.422022192Z",
                        "signature": "6cXaTBHR1SIfj/kCQqVKIy2y702T6U+pg/IWulyvZKB1BcY7y0d3MPz3PmNsl5aV69/jvz1F21v3hoQsKQJECQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "B59D3818B5030B39FF2D9AF2A2C823333C1A9B78",
                        "timestamp": "2025-01-15T08:45:13.434972734Z",
                        "signature": "73/E8L88lTrsZGQcy5waWHx7HRZeWIIaEhwvGwD5SIfrMRMWiYb5Bck7JWQFLnRhB6VAbVBIVpANSOUJxTQeBw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "1A86BFBC6B28EACDD5E0522A0A02F213506FD5F3",
                        "timestamp": "2025-01-15T08:45:13.521219731Z",
                        "signature": "30kxZ+CCkw6eikP14ZqMco2KHFebndCHEkziqWRTY/GJfVUwcWQImsV+m0bvwrDprf7GU8LOTQOeyoNlhJ+uBw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "B9F4C7A240A54FB28FEFDAA95623A0C41F78CD06",
                        "timestamp": "2025-01-15T08:45:13.062730267Z",
                        "signature": "cQ9wLF0k9lXuHpVU6i3E1+Jv9czQr24M2zieXORH04CtzSsE52jo0/DvZydjt7t8+mN/MjQzjf1dTJvv+GCrBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "C5185BCF3AD9E4B90E1103D7EBCEB503AE3E263D",
                        "timestamp": "2025-01-15T08:45:13.445360737Z",
                        "signature": "aSXwujLodyvvDwai2BABixHg+zGHNI5PVovHzFNv10WBhpE1tNRUknia6dOWj+P84p1jBnQB3u3+E1FW98muAQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "B710EE0B854C93C1AF657D2F2A56D42D01205245",
                        "timestamp": "2025-01-15T08:45:13.447605852Z",
                        "signature": "XKaV2bU3i0inwO6uSMj3RRpIyrukSi80WwZwjczITthaN/kkm4lERgyAhF+FepbcK9eV1zIe4C/n2Rqoa80gAg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "CB55FF4C609E11A0C417D95A0F697F3B33284BA6",
                        "timestamp": "2025-01-15T08:45:13.418756919Z",
                        "signature": "AVXf+Zw4uLzIbsjIvnTAsEstI76jDgtp3fFK+fWjTTGlO5VbCx076NcKhYyEKUMaOhDPBEAbQpfOPXrYZjbzDQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "620924E751600A5222017221FD7066E8DF0C38DF",
                        "timestamp": "2025-01-15T08:45:13.474660603Z",
                        "signature": "N6tsyUpKAVnfGLC2i/hWfm9zFJgInUHSJvVeHbhO533MuxY5KpIojAtStWJWnntQtw5wG79vkftQPuGinckTAQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "3835FDDA7D3C8DB75A233494C950C5916219B1B9",
                        "timestamp": "2025-01-15T08:45:13.426546427Z",
                        "signature": "ddt2IdPvxpNivVxVzY3jIjlXGN/DYmabCj8pHR6bHyXQ/FvPQFa9JeFAHhh8l9AvwycmfncvJhZWRWmJmFWuDA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "9FBFCDFF95858685E5E51CDD46D4C91DB5392C99",
                        "timestamp": "2025-01-15T08:45:13.478412637Z",
                        "signature": "iWd9yQ/lZ+onTW0B1/nahG/oqVrIV747z9lO0sV1lHNc7qDpFPITDVo/ex7gjeYhAGjq88HZZSy/IwiEh0rrDQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "800FE546B30EF262E17068B98957920A7F7ADCAA",
                        "timestamp": "2025-01-15T08:45:13.455217363Z",
                        "signature": "2tsWw0QmNL7XcfGPg7tSEGW5DP7aE74iIzrZJhlYDUQwnT2iP4JbaY1wz24UEUeVrOgTogvNvuLIdBsBBSFGBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "06A934471FD8CD6BF983AB2208DFF8B683605B53",
                        "timestamp": "2025-01-15T08:45:13.422442837Z",
                        "signature": "ehnj/xZnaqZQvXx0dYnya8s5Ett2P95N/A8NpKjB+8wMi0qRQA8T1FzmeTbz42/sMLyBEKHSayDY1jnFqfRzDw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "18042A417D9175BD0A3D02826A9D7FE40EA2D111",
                        "timestamp": "2025-01-15T08:45:13.569778984Z",
                        "signature": "Har2CtpLZtJzh0aetwiVKn0aACjurVgF666AP8P5sAVG0AAQQ+8Tz5Aen0O/Vdbq7q2zEooA+fvydqaOHicfDQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "A3513488C04FED0BD7CCFB9EC9EBC6D98AEE35B0",
                        "timestamp": "2025-01-15T08:45:13.522704243Z",
                        "signature": "NmNPRBXqy2zs6jLcRRNtU+gBFICgXpk+9hQ/WETzxCeODzgtYfvaIQjXBhijjqmHWTnX6z9ywxp98n4y7VnpCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "6675542B68D334FD23273DCD58223AD54700B1BD",
                        "timestamp": "2025-01-15T08:45:13.462661815Z",
                        "signature": "R4w71Q+mQfnUt1QeghRV3uagwFHyV84nsY3HVPHtp4JMt0nUTD+yCG7+3XS8M2eoz/Y1HAw3UNUTV7+Stt9dCw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "2C29874572B01497C5172E55E0FEF80E105DB4EC",
                        "timestamp": "2025-01-15T08:45:13.53683194Z",
                        "signature": "efQTkmdyR8BRnNLKo5GtAb1l3GEAkQSOts5mE1cKyibWxcawWb/wq9iLFeGaIjjZOT99kn/Gwix4BxbaRrhDAw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "A2FA96ABE3A05B48FFA603694512B513BABE70CB",
                        "timestamp": "2025-01-15T08:45:13.64029191Z",
                        "signature": "ZQUlRcWNZp68K0C/7l5dCSww4DMce5afWGElzLhdeZ0sw/bPxuOez3/wMq4BrHM20W4TV3jme/GawleXIZTSBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "150708B520627549A35B34AF8E1054CF0B2F695E",
                        "timestamp": "2025-01-15T08:45:13.442510246Z",
                        "signature": "GpcVEEgteA1CzhfxsO1H/IOPWqlSeeSgkC5T9W9i7hB2xHeyQEV5LP7FSIrJk3437O7O9LFNUcC+MxKSJyRRDA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "2F5621A9CB2B9D14F696CE085AD261ED1A628153",
                        "timestamp": "2025-01-15T08:45:13.430429828Z",
                        "signature": "6rwoBlugjRXQDkPOAr/8wenN+15CE5ITbUQswQERMbvGHiI/w/bkrVaWDSY2ATHHOMNXYNI/DOLahT4GPGIHDg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "A5A57699ED5519B2B1521EBBD4B5E4E49397A898",
                        "timestamp": "2025-01-15T08:45:13.428072703Z",
                        "signature": "j0T58jpfVopS3kI/Bt5G3WtJrXcNtXTZl7mFVCZLgT2YxNN8aE5dnDGAHGCgQCAFv+M6mAZzre7ue+c2vr/YAg=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "C67AA20E0F092159E8033332EE430C37F6F1441C",
                        "timestamp": "2025-01-15T08:45:13.468165222Z",
                        "signature": "+DlE88Y6fRvqh6QAcGVzumRGJeqQf1pmh5ygL3vCrfx1PJx5q6gc3RPO+04qu5IuV5CUeI0bnHcTzlNiRqTaAA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "9814652033452AEAC7F2501708BBB601D7873C80",
                        "timestamp": "2025-01-15T08:45:13.434966185Z",
                        "signature": "ghaCWSOadud6QfXcPKLyGLt6wWH3sVTC1AIQTcntz5dMnuImvChwC9qMQChLa1OUECGkEmJY4ROe5rSoqnO4DQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "6FD2BA3BA00E6AB6BF43B0A7FBE486C541288F99",
                        "timestamp": "2025-01-15T08:45:13.435087217Z",
                        "signature": "jYkq6vtRH4VxLQKAT8jxstIPb8KF4gjkY7v+97dC+/xhA8XYQ9GyPbLN5nsHD0BjL0vQ+MGe0RxuJd/mptR9DQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "14A20AA53BDBF26BB22B9A62D56ED600553D4C15",
                        "timestamp": "2025-01-15T08:45:13.384680948Z",
                        "signature": "NelGNMhkAWZ93cNn36ZJqwXVB4t3URE7dvgCObJMLrNg9xkqzcMWz8Xn8Sul8KIXs8VBOQ/rxs0Th7OMVDplBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "3D781000ED6DE85956B23AB6BDC3E192A5E4D606",
                        "timestamp": "2025-01-15T08:45:13.43385876Z",
                        "signature": "DitQ0JoKATppu0/QCvCzCiF7WJNl4j/QKWdcgcwb4krAJdscpi6NRmCoa83Tky1c9e+xW9a7c/sqXCDLpB0FBA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "95D4821111AEA9045EB4A6E6EB38BC70F511DD98",
                        "timestamp": "2025-01-15T08:45:13.441532674Z",
                        "signature": "a4B+xa+uFH3GYy4DmBEZlur8yFHmt24g8SpgNGEhU01LyPngvT6BKSXTLAQo5KGw7DNB+bYI8t/Wem8AcKmkDA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "777EE6A3B89152EBF8994A56FE10ED3AADA924D9",
                        "timestamp": "2025-01-15T08:45:13.433104802Z",
                        "signature": "A4hnd7QwHnO8USCu6X+AAUyewbeVTJ1DkTld3ZRwfZ002+iij3jc+Az+ZL7H7F7wTiaqE1iN1rfopsj8YtUOCQ=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "0AB7E7DB919482E82228E6720D6A0DA1B546B477",
                        "timestamp": "2025-01-15T08:45:13.501118965Z",
                        "signature": "fJsAAmUQZii7bzRtfHeEFBhwaX3NSiZ+hRq5m11AOs69Hx7ohEY8zO1kvrYmm5vmjFPvSockvmAwaLlKf1JRDw=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "4CEEAB2CCAA9E9CD5EAB94238F7AF4658C364605",
                        "timestamp": "2025-01-15T08:45:13.535744274Z",
                        "signature": "djhDCRUv0JXdu5ds8fdDlj4ssxOR41WR/k2V29zYrOGuE/E9jhagvq64ECXaaMAaulLkNAbuwESL2THeVDe3DA=="
                    },
                    {
                        "block_id_flag": 2,
                        "validator_address": "ACAB12936A238CE7F4B521871F907FF6A9729282",
                        "timestamp": "2025-01-15T08:45:13.513377758Z",
                        "signature": "1XQDoafCWmoR/SpwTFw5QC6ETfQ9q18mZ4gy9O+YQ/pnBz6T2kZwYqtNkYFvbuNsJ4cW6uCLjiUPeQ7vfGaRCQ=="
                    }
                ]
            }
        }
    }
}

# Extract signatures from the JSON block
signatures = block_data["result"]["block"]["last_commit"]["signatures"]

signatures_size = sys.getsizeof(json.dumps(signatures))

# Calculate total size of the block (as JSON)
block_size = sys.getsizeof(json.dumps(block_data))

# Calculate size for non-signature data
non_signature_size = block_size - signatures_size

# Convert to kilobytes (KB)
signature_kb = signatures_size / 1024
non_signature_kb = non_signature_size / 1024
block_kb = block_size / 1024

print (f"Signature size: {signature_kb:.2f} KB")
print (f"Non-signature size: {non_signature_kb:.2f} KB")
print (f"Total size: {block_kb:.2f} KB")
signature_kb, non_signature_kb
